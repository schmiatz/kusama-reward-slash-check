import requests
import sys
import json
from datetime import datetime
from collections import defaultdict

def get_latest_block():
    url = "https://kusama.api.subscan.io/api/v2/scan/blocks"
    headers = {'Content-Type': 'application/json'}
    data = {"page": 0, "row": 1}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data['data']['blocks'][0]['block_num']

def get_historical_price(coin, currency, timestamp, api_key):
    url = f"https://min-api.cryptocompare.com/data/pricehistorical"
    payload = {
        'fsym': coin,
        'tsyms': currency,
        'ts': timestamp,
        'api_key': api_key
    }
    response = requests.get(url, params=payload)
    data = response.json()
    price = data[coin][currency]
    return price

def fetch_rewards_and_slashes(address, latest_block, api_key=None):
    base_url = "https://kusama.api.subscan.io/api/scan/account/reward_slash"
    headers = {'Content-Type': 'application/json'}
    page = 0
    results_per_page = 10
    has_more = True
    all_entries = []

    while has_more:
        body = {
            "address": address,
            "block_range": f"1-{latest_block}",
            "is_stash": True,
            "page": page,
            "row": results_per_page,
            "timeout": 0
        }
        response = requests.post(base_url, json=body, headers=headers)
        response.raise_for_status()
        data = response.json()
        rewards_slashes = data['data']['list']

        if not rewards_slashes:
            break

        for entry in rewards_slashes:
            event_type = "Reward" if entry['event_id'].startswith("Reward") else "Slash"
            amount_in_ksm = float(entry["amount"]) / 1000000000000
            date = datetime.utcfromtimestamp(entry["block_timestamp"])
            formatted_date = date.strftime('%d-%m-%y')
            month_year = date.strftime('%B %Y')
            year = date.strftime('%Y')
            extrinsic_hash = entry.get("extrinsic_hash", "N/A")
            if api_key:
                price = get_historical_price("KSM", "EUR", entry["block_timestamp"], api_key)
                earned_value = amount_in_ksm * price
                entry_data = (year, month_year, event_type, amount_in_ksm, formatted_date, extrinsic_hash, price, earned_value)
            else:
                entry_data = (year, month_year, event_type, amount_in_ksm, formatted_date, extrinsic_hash)
            all_entries.append(entry_data)

        page += 1
        has_more = len(rewards_slashes) == results_per_page

    return all_entries

def print_sorted_entries(entries, api_key=None):
    grouped_by_month = defaultdict(list)
    month_sums = defaultdict(float)
    month_earned_values = defaultdict(float)
    year_sums = defaultdict(float)
    year_earned_values = defaultdict(float)

    for entry in entries:
        if api_key and len(entry) == 8:
            year, month_year, event_type, amount, formatted_date, extrinsic_hash, price, earned_value = entry
            grouped_by_month[month_year].append(f'{event_type}: "{amount:.12f} KSM", Date: "{formatted_date}", Transaction: "{extrinsic_hash}", Daily average Price: {price:.2f} €, Earned Value: {earned_value:.2f} €')
            if event_type == "Reward":
                month_sums[month_year] += amount
                year_sums[year] += amount
                month_earned_values[month_year] += earned_value
                year_earned_values[year] += earned_value
            elif event_type == "Slash":
                month_sums[month_year] -= amount
                year_sums[year] -= amount
                month_earned_values[month_year] -= earned_value
                year_earned_values[year] -= earned_value
        else:
            year, month_year, event_type, amount, formatted_date, extrinsic_hash = entry
            grouped_by_month[month_year].append(f'{event_type}: "{amount:.12f} KSM", Date: "{formatted_date}", Transaction: "{extrinsic_hash}"')
            if event_type == "Reward":
                month_sums[month_year] += amount
                year_sums[year] += amount
            elif event_type == "Slash":
                month_sums[month_year] -= amount
                year_sums[year] -= amount

    for month in sorted(grouped_by_month.keys(), key=lambda x: datetime.strptime(x, "%B %Y")):
        print(f'{month}:')
        for entry in grouped_by_month[month]:
            print(entry)
        if api_key:
            print(f'Summary: "{month_sums[month]:.12f} KSM", Earned Value: {month_earned_values[month]:.2f} €\n')
        else:
            print(f'Summary: "{month_sums[month]:.12f} KSM"\n')

    # Print summaries for each year after the last month of each year
    for year in sorted(year_sums):
        if api_key:
            print(f'Summary Year {year}: {year_sums[year]:.12f} KSM, Earned Value: {year_earned_values[year]:.2f} €')
        else:
            print(f'Summary Year {year}: {year_sums[year]:.12f} KSM')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 kusama-get-rewards.py <Kusama Address> [API Key]")
        sys.exit(1)

    address = sys.argv[1]
    api_key = sys.argv[2] if len(sys.argv) > 2 else None
    latest_block = get_latest_block()
    entries = fetch_rewards_and_slashes(address, latest_block, api_key)
    print_sorted_entries(entries, api_key)
