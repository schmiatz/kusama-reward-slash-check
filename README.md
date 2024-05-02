# kusama-reward-slash-check

This script checks the rewards and slashes for a Kusama Collator and calculates the earned amount in Fiat Money.   

## Requirements

You need to have the python package requests installed.   

## How to use

Run the script while providing your Kusama Collators Public Stash Key if you dont need the fiat prices:   
`python3 kusama-get-rewards.py <PUBKEY>`

Run the script while providing your Kusama Collators Public Stash Key and your API key from cryptocompare.com to get the fiat amounts calculated:   
`python3 kusama-get-rewards.py <PUBKEY> <API-KEY>`
