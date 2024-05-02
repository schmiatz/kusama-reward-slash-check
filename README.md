# kusama-reward-slash-check

This script checks the rewards and slashes for a Kusama Collator and calculates the earned amount in Fiat Money.   

## Requirements

You need to have the python package requests installed.   

## How to use

Run the script while providing your Kusama Collators Public Stash Key if you dont need the fiat prices:   
`python3 kusama-get-rewards.py <PUBKEY>`

Run the script while providing your Kusama Collators Public Stash Key and your API key from cryptocompare.com to get the fiat amounts calculated:   
`python3 kusama-get-rewards.py <PUBKEY> <API-KEY>`

## Example Output
### With API Key
```
March 2024:
Reward: "0.192805173840 KSM", Date: "31-03-24", Transaction: "0x889c369084bd966b83cb6050bb28e3f81ccf9d7df285fb9f7029d9a31949e730", Daily average Price: 44.91 €, Earned Value: 8.66 €
Reward: "0.004716748581 KSM", Date: "31-03-24", Transaction: "0x13b8c5389797125fb094948e029a6726eebe6e8bb4da0b7f48b814b1873812c3", Daily average Price: 44.91 €, Earned Value: 0.21 €
Reward: "0.280429561333 KSM", Date: "31-03-24", Transaction: "0x490bbcf0c8b9b7d7793d9519bfec95190dbf8b8f6db36688c353d96493ef661b", Daily average Price: 44.91 €, Earned Value: 12.59 €
Reward: "0.006510590210 KSM", Date: "31-03-24", Transaction: "0xfe1b39e5896a0566c17658ddc0b1c51e6c03167745d968c1d8d7ff0e02868f16", Daily average Price: 44.91 €, Earned Value: 0.29 €
Summary: "0.484462073964 KSM", Earned Value: 21.76 €

April 2024:
Reward: "0.001850320708 KSM", Date: "28-04-24", Transaction: "0x6e43bb414856023bae502287c7645030901fe1afc3041a4d39a855d5c19f5919", Daily average Price: 27.65 €, Earned Value: 0.05 €
Reward: "0.024829056262 KSM", Date: "28-04-24", Transaction: "0x60db806aad6bde85217011614d2b593546d53e00b579b17eec059eee7784a37c", Daily average Price: 27.65 €, Earned Value: 0.69 €
Reward: "0.251911923208 KSM", Date: "28-04-24", Transaction: "0x145c20fba742b4b69a99a798cc405ca3ccb43e68c4365f15843d57773043e7ff", Daily average Price: 27.65 €, Earned Value: 6.97 €
Reward: "0.209772114401 KSM", Date: "28-04-24", Transaction: "0xbec32c68afbdb8756a2bd985b28f0417e25a957193a58f83dd6138de9f0f4e99", Daily average Price: 27.65 €, Earned Value: 5.80 €
Reward: "0.162906024878 KSM", Date: "28-04-24", Transaction: "0x3ae97d00700abd124b40a56dbabf0aef82fc3fba2192cbcab8332f6acb324a96", Daily average Price: 27.65 €, Earned Value: 4.50 €
Reward: "0.140212456933 KSM", Date: "28-04-24", Transaction: "0x5fea786176d519ab2c6681e7dea217cd90f288d752814ebf0f8cccb20c432bb4", Daily average Price: 27.65 €, Earned Value: 3.88 €
Reward: "0.198282734499 KSM", Date: "28-04-24", Transaction: "0x3ccb4a47864bf54febb54e64699bc223c8ba0edbd8c2a414d2a14a43f09f66a7", Daily average Price: 27.65 €, Earned Value: 5.48 €
Reward: "0.088750620875 KSM", Date: "28-04-24", Transaction: "0xd229bcf4a6ab51576a5ba3a52180c57dae4d2164cd2ee0fff5f909fe1a9b7a3c", Daily average Price: 27.65 €, Earned Value: 2.45 €
Reward: "0.065377754288 KSM", Date: "28-04-24", Transaction: "0x92d01720ecb3f3a6a0d75c606fb43ff2aa1578e2ee634f84242033f2cc40196f", Daily average Price: 27.65 €, Earned Value: 1.81 €
Reward: "0.094538262856 KSM", Date: "28-04-24", Transaction: "0x86a8f137f40caca96dacd78c1095c6f2b7304c3487164f9995cf689cb2cc0ccc", Daily average Price: 27.65 €, Earned Value: 2.61 €
Reward: "0.116455606630 KSM", Date: "28-04-24", Transaction: "0x86a8f137f40caca96dacd78c1095c6f2b7304c3487164f9995cf689cb2cc0ccc", Daily average Price: 27.65 €, Earned Value: 3.22 €
Reward: "0.126170278459 KSM", Date: "27-04-24", Transaction: "0xf2ebfcd556533d2c5878faa1d721458608095e6a4993d82139eab33656617934", Daily average Price: 27.88 €, Earned Value: 3.52 €
Reward: "0.144936764961 KSM", Date: "27-04-24", Transaction: "0x13bf4b99a1aec4e2bc30a4ca29cc1b41311e89fd6c8aaea50ec3f1ee39da0c55", Daily average Price: 27.88 €, Earned Value: 4.04 €
Reward: "0.049187356103 KSM", Date: "27-04-24", Transaction: "0x13bf4b99a1aec4e2bc30a4ca29cc1b41311e89fd6c8aaea50ec3f1ee39da0c55", Daily average Price: 27.88 €, Earned Value: 1.37 €
Reward: "0.073003537143 KSM", Date: "27-04-24", Transaction: "0x13bf4b99a1aec4e2bc30a4ca29cc1b41311e89fd6c8aaea50ec3f1ee39da0c55", Daily average Price: 27.88 €, Earned Value: 2.04 €
Reward: "0.122612921166 KSM", Date: "26-04-24", Transaction: "0x5e44ede0ee98406b25fecbbac75f07966b189b28a249edf411e280b47bfab15b", Daily average Price: 26.98 €, Earned Value: 3.31 €
Reward: "0.207825994799 KSM", Date: "26-04-24", Transaction: "0x5527b4a4102f129feb26bfcab862d1df33efcb04b32611749593a8e04da0dada", Daily average Price: 26.98 €, Earned Value: 5.61 €
Reward: "0.382244622504 KSM", Date: "26-04-24", Transaction: "0x5527b4a4102f129feb26bfcab862d1df33efcb04b32611749593a8e04da0dada", Daily average Price: 26.98 €, Earned Value: 10.31 €
Reward: "0.176739883405 KSM", Date: "26-04-24", Transaction: "0x5527b4a4102f129feb26bfcab862d1df33efcb04b32611749593a8e04da0dada", Daily average Price: 26.98 €, Earned Value: 4.77 €
Reward: "0.079276998173 KSM", Date: "25-04-24", Transaction: "0xb4f5f58e1401c56937c78a5cab6b3b74fcf54b2e43a22e566b328d75fc661d0b", Daily average Price: 27.83 €, Earned Value: 2.21 €
Reward: "0.156446812999 KSM", Date: "25-04-24", Transaction: "0x936e4447473f51a393be1fbaec2a318efb33fcd7d3d675e3496e995dedb6f2c5", Daily average Price: 27.83 €, Earned Value: 4.35 €
Reward: "0.073422790313 KSM", Date: "25-04-24", Transaction: "0xa40773071cac98baaf00c7136c26125baf9ab99b17bcbe69456ec7a68a136a1b", Daily average Price: 27.83 €, Earned Value: 2.04 €
Reward: "0.100895561871 KSM", Date: "25-04-24", Transaction: "0xa40773071cac98baaf00c7136c26125baf9ab99b17bcbe69456ec7a68a136a1b", Daily average Price: 27.83 €, Earned Value: 2.81 €
Reward: "0.107148800463 KSM", Date: "25-04-24", Transaction: "0x6dc1addd0adabb790bda0a89f29f5c9c9ad85e90683d65cd1a1216358cd06fc2", Daily average Price: 27.83 €, Earned Value: 2.98 €
Reward: "0.202941115017 KSM", Date: "25-04-24", Transaction: "0x6dc1addd0adabb790bda0a89f29f5c9c9ad85e90683d65cd1a1216358cd06fc2", Daily average Price: 27.83 €, Earned Value: 5.65 €
Reward: "0.340109783709 KSM", Date: "25-04-24", Transaction: "0x6dc1addd0adabb790bda0a89f29f5c9c9ad85e90683d65cd1a1216358cd06fc2", Daily average Price: 27.83 €, Earned Value: 9.47 €
Reward: "0.211302009785 KSM", Date: "25-04-24", Transaction: "0x6dc1addd0adabb790bda0a89f29f5c9c9ad85e90683d65cd1a1216358cd06fc2", Daily average Price: 27.83 €, Earned Value: 5.88 €
Reward: "0.118578807005 KSM", Date: "25-04-24", Transaction: "0x23bdda9d139992c8ea26a31413cf76f117799efb7df748081db4cfc3fde69b33", Daily average Price: 27.83 €, Earned Value: 3.30 €
Reward: "0.253482880327 KSM", Date: "25-04-24", Transaction: "0x23bdda9d139992c8ea26a31413cf76f117799efb7df748081db4cfc3fde69b33", Daily average Price: 27.83 €, Earned Value: 7.05 €
Reward: "0.081785481467 KSM", Date: "25-04-24", Transaction: "0x23bdda9d139992c8ea26a31413cf76f117799efb7df748081db4cfc3fde69b33", Daily average Price: 27.83 €, Earned Value: 2.28 €
Reward: "0.197419268952 KSM", Date: "25-04-24", Transaction: "0x23bdda9d139992c8ea26a31413cf76f117799efb7df748081db4cfc3fde69b33", Daily average Price: 27.83 €, Earned Value: 5.49 €
Reward: "0.001413217806 KSM", Date: "25-04-24", Transaction: "0x1d786a2997f8fbccab69d3e98718a29783fb4a481b9c857c3d08087ecba5b92e", Daily average Price: 27.83 €, Earned Value: 0.04 €
Reward: "0.006419091931 KSM", Date: "19-04-24", Transaction: "0x54886b6b6b9eb179665261e23206226b9d2bf97f5414fab4e881f1d16e671a8d", Daily average Price: 29.34 €, Earned Value: 0.19 €
Reward: "0.097147915589 KSM", Date: "13-04-24", Transaction: "0x71fce0dba6d7e35551594fa4607e8beb516c546e53036d2faabe7f23a7564f1b", Daily average Price: 27.47 €, Earned Value: 2.67 €
Reward: "0.029188180114 KSM", Date: "13-04-24", Transaction: "0x867dc2d5f01b81e602f8f36d3e2fb19e597dc402722a1a485c07edce56c29070", Daily average Price: 27.47 €, Earned Value: 0.80 €
Reward: "0.471251429733 KSM", Date: "12-04-24", Transaction: "0x47db247b3ef33aec519b547f4becc2502f719df3374c4d7c57cfbd0a8b727e50", Daily average Price: 31.69 €, Earned Value: 14.93 €
Reward: "0.049604763323 KSM", Date: "12-04-24", Transaction: "0xc864904741aef8bf265ac7799aeaab3487ed978c107bd772defc3b6eff074e16", Daily average Price: 31.69 €, Earned Value: 1.57 €
Reward: "0.275225255259 KSM", Date: "12-04-24", Transaction: "0x4d6ea1f31d639332ed59b3e4141b8c9490a913a91b419bc77cd1bd8bade898e0", Daily average Price: 31.69 €, Earned Value: 8.72 €
Reward: "0.234696774029 KSM", Date: "12-04-24", Transaction: "0xb8a4e92c2d229fec44d8504787e3231ee6734c5b674cde22eb4d38a08169acb0", Daily average Price: 31.69 €, Earned Value: 7.44 €
Reward: "0.209174410238 KSM", Date: "11-04-24", Transaction: "0x068f12927126eeb6c146f249d45dcc7d17fbc96381cd3496132c2af087087bb8", Daily average Price: 37.13 €, Earned Value: 7.77 €
Reward: "0.236433298903 KSM", Date: "11-04-24", Transaction: "0xf2cc81fadb03aba4eae4c0b552bcfa4a86e0f8e9293a0ec1a4d4c1ae57d62b27", Daily average Price: 37.13 €, Earned Value: 8.78 €
Reward: "0.137144526628 KSM", Date: "11-04-24", Transaction: "0xa4858e339bcc3397c1cb20d08a27f9a264dab4ebde87f5e7d5a94a1219381d15", Daily average Price: 37.13 €, Earned Value: 5.09 €
Reward: "0.132036418708 KSM", Date: "11-04-24", Transaction: "0x1668128f207faf3aa72a6fe88923873dd69b70ad8b568116b31f5098f23289f7", Daily average Price: 37.13 €, Earned Value: 4.90 €
Reward: "0.101015762257 KSM", Date: "02-04-24", Transaction: "0xc840524d2d6330c1143cc7b49f0a96dbde639a66695b9887e5bbf55c4d3c56e6", Daily average Price: 39.51 €, Earned Value: 3.99 €
Reward: "0.053573836054 KSM", Date: "02-04-24", Transaction: "0x3c7830967803c7d87b435838f2abd9522d0327248200ce85b36c4455924551ae", Daily average Price: 39.51 €, Earned Value: 2.12 €
Reward: "0.124693798142 KSM", Date: "02-04-24", Transaction: "0x9bbff4d2ff16ce98e96fd40ed2dae30619a91fcabd837f6335a649852685d800", Daily average Price: 39.51 €, Earned Value: 4.93 €
Reward: "0.124755358659 KSM", Date: "01-04-24", Transaction: "0xea059691c0af7346da8b72555d66f338a7be80b15ef6720ea376b73cf1329c60", Daily average Price: 43.16 €, Earned Value: 5.38 €
Reward: "0.001539399510 KSM", Date: "01-04-24", Transaction: "0xdf9c76d7562a6ed11d9badeca7b2e4ff50ed26951d16012c2fd6c7eba4a360d6", Daily average Price: 43.16 €, Earned Value: 0.07 €
Reward: "0.175404734587 KSM", Date: "01-04-24", Transaction: "0x4d6bad38e0f6551b386bc0e11ecd1c6d84b656cc7e1735f664bf785c4f2d80fd", Daily average Price: 43.16 €, Earned Value: 7.57 €
Reward: "0.105196861584 KSM", Date: "01-04-24", Transaction: "0x24370bb79c016a54c33ade4ca488826a2d5ec835322751bc8535dc4e3c5428b9", Daily average Price: 43.16 €, Earned Value: 4.54 €
Summary: "7.126333577213 KSM", Earned Value: 217.44 €

May 2024:
Reward: "0.404827965013 KSM", Date: "02-05-24", Transaction: "0xb0eb8a82b4cf0caa69e9ad22729a0ae6fdea1101d0fab61cf16b14198cb771db", Daily average Price: 27.53 €, Earned Value: 11.14 €
Summary: "0.404827965013 KSM", Earned Value: 11.14 €

Summary Year 2024: 8.015623616190 KSM, Earned Value: 250.34 €
```

### Without API Key
```
March 2024:
Reward: "0.192805173840 KSM", Date: "31-03-24", Transaction: "0x889c369084bd966b83cb6050bb28e3f81ccf9d7df285fb9f7029d9a31949e730"
Reward: "0.004716748581 KSM", Date: "31-03-24", Transaction: "0x13b8c5389797125fb094948e029a6726eebe6e8bb4da0b7f48b814b1873812c3"
Reward: "0.280429561333 KSM", Date: "31-03-24", Transaction: "0x490bbcf0c8b9b7d7793d9519bfec95190dbf8b8f6db36688c353d96493ef661b"
Reward: "0.006510590210 KSM", Date: "31-03-24", Transaction: "0xfe1b39e5896a0566c17658ddc0b1c51e6c03167745d968c1d8d7ff0e02868f16"
Summary: "0.484462073964 KSM"

April 2024:
Reward: "0.001850320708 KSM", Date: "28-04-24", Transaction: "0x6e43bb414856023bae502287c7645030901fe1afc3041a4d39a855d5c19f5919"
Reward: "0.024829056262 KSM", Date: "28-04-24", Transaction: "0x60db806aad6bde85217011614d2b593546d53e00b579b17eec059eee7784a37c"
Reward: "0.251911923208 KSM", Date: "28-04-24", Transaction: "0x145c20fba742b4b69a99a798cc405ca3ccb43e68c4365f15843d57773043e7ff"
Reward: "0.209772114401 KSM", Date: "28-04-24", Transaction: "0xbec32c68afbdb8756a2bd985b28f0417e25a957193a58f83dd6138de9f0f4e99"
Reward: "0.162906024878 KSM", Date: "28-04-24", Transaction: "0x3ae97d00700abd124b40a56dbabf0aef82fc3fba2192cbcab8332f6acb324a96"
Reward: "0.140212456933 KSM", Date: "28-04-24", Transaction: "0x5fea786176d519ab2c6681e7dea217cd90f288d752814ebf0f8cccb20c432bb4"
Reward: "0.198282734499 KSM", Date: "28-04-24", Transaction: "0x3ccb4a47864bf54febb54e64699bc223c8ba0edbd8c2a414d2a14a43f09f66a7"
Reward: "0.088750620875 KSM", Date: "28-04-24", Transaction: "0xd229bcf4a6ab51576a5ba3a52180c57dae4d2164cd2ee0fff5f909fe1a9b7a3c"
Reward: "0.065377754288 KSM", Date: "28-04-24", Transaction: "0x92d01720ecb3f3a6a0d75c606fb43ff2aa1578e2ee634f84242033f2cc40196f"
Reward: "0.094538262856 KSM", Date: "28-04-24", Transaction: "0x86a8f137f40caca96dacd78c1095c6f2b7304c3487164f9995cf689cb2cc0ccc"
Reward: "0.116455606630 KSM", Date: "28-04-24", Transaction: "0x86a8f137f40caca96dacd78c1095c6f2b7304c3487164f9995cf689cb2cc0ccc"
Reward: "0.126170278459 KSM", Date: "27-04-24", Transaction: "0xf2ebfcd556533d2c5878faa1d721458608095e6a4993d82139eab33656617934"
Reward: "0.144936764961 KSM", Date: "27-04-24", Transaction: "0x13bf4b99a1aec4e2bc30a4ca29cc1b41311e89fd6c8aaea50ec3f1ee39da0c55"
Reward: "0.049187356103 KSM", Date: "27-04-24", Transaction: "0x13bf4b99a1aec4e2bc30a4ca29cc1b41311e89fd6c8aaea50ec3f1ee39da0c55"
Reward: "0.073003537143 KSM", Date: "27-04-24", Transaction: "0x13bf4b99a1aec4e2bc30a4ca29cc1b41311e89fd6c8aaea50ec3f1ee39da0c55"
Reward: "0.122612921166 KSM", Date: "26-04-24", Transaction: "0x5e44ede0ee98406b25fecbbac75f07966b189b28a249edf411e280b47bfab15b"
Reward: "0.207825994799 KSM", Date: "26-04-24", Transaction: "0x5527b4a4102f129feb26bfcab862d1df33efcb04b32611749593a8e04da0dada"
Reward: "0.382244622504 KSM", Date: "26-04-24", Transaction: "0x5527b4a4102f129feb26bfcab862d1df33efcb04b32611749593a8e04da0dada"
Reward: "0.176739883405 KSM", Date: "26-04-24", Transaction: "0x5527b4a4102f129feb26bfcab862d1df33efcb04b32611749593a8e04da0dada"
Reward: "0.079276998173 KSM", Date: "25-04-24", Transaction: "0xb4f5f58e1401c56937c78a5cab6b3b74fcf54b2e43a22e566b328d75fc661d0b"
Reward: "0.156446812999 KSM", Date: "25-04-24", Transaction: "0x936e4447473f51a393be1fbaec2a318efb33fcd7d3d675e3496e995dedb6f2c5"
Reward: "0.073422790313 KSM", Date: "25-04-24", Transaction: "0xa40773071cac98baaf00c7136c26125baf9ab99b17bcbe69456ec7a68a136a1b"
Reward: "0.100895561871 KSM", Date: "25-04-24", Transaction: "0xa40773071cac98baaf00c7136c26125baf9ab99b17bcbe69456ec7a68a136a1b"
Reward: "0.107148800463 KSM", Date: "25-04-24", Transaction: "0x6dc1addd0adabb790bda0a89f29f5c9c9ad85e90683d65cd1a1216358cd06fc2"
Reward: "0.202941115017 KSM", Date: "25-04-24", Transaction: "0x6dc1addd0adabb790bda0a89f29f5c9c9ad85e90683d65cd1a1216358cd06fc2"
Reward: "0.340109783709 KSM", Date: "25-04-24", Transaction: "0x6dc1addd0adabb790bda0a89f29f5c9c9ad85e90683d65cd1a1216358cd06fc2"
Reward: "0.211302009785 KSM", Date: "25-04-24", Transaction: "0x6dc1addd0adabb790bda0a89f29f5c9c9ad85e90683d65cd1a1216358cd06fc2"
Reward: "0.118578807005 KSM", Date: "25-04-24", Transaction: "0x23bdda9d139992c8ea26a31413cf76f117799efb7df748081db4cfc3fde69b33"
Reward: "0.253482880327 KSM", Date: "25-04-24", Transaction: "0x23bdda9d139992c8ea26a31413cf76f117799efb7df748081db4cfc3fde69b33"
Reward: "0.081785481467 KSM", Date: "25-04-24", Transaction: "0x23bdda9d139992c8ea26a31413cf76f117799efb7df748081db4cfc3fde69b33"
Reward: "0.197419268952 KSM", Date: "25-04-24", Transaction: "0x23bdda9d139992c8ea26a31413cf76f117799efb7df748081db4cfc3fde69b33"
Reward: "0.001413217806 KSM", Date: "25-04-24", Transaction: "0x1d786a2997f8fbccab69d3e98718a29783fb4a481b9c857c3d08087ecba5b92e"
Reward: "0.006419091931 KSM", Date: "19-04-24", Transaction: "0x54886b6b6b9eb179665261e23206226b9d2bf97f5414fab4e881f1d16e671a8d"
Reward: "0.097147915589 KSM", Date: "13-04-24", Transaction: "0x71fce0dba6d7e35551594fa4607e8beb516c546e53036d2faabe7f23a7564f1b"
Reward: "0.029188180114 KSM", Date: "13-04-24", Transaction: "0x867dc2d5f01b81e602f8f36d3e2fb19e597dc402722a1a485c07edce56c29070"
Reward: "0.471251429733 KSM", Date: "12-04-24", Transaction: "0x47db247b3ef33aec519b547f4becc2502f719df3374c4d7c57cfbd0a8b727e50"
Reward: "0.049604763323 KSM", Date: "12-04-24", Transaction: "0xc864904741aef8bf265ac7799aeaab3487ed978c107bd772defc3b6eff074e16"
Reward: "0.275225255259 KSM", Date: "12-04-24", Transaction: "0x4d6ea1f31d639332ed59b3e4141b8c9490a913a91b419bc77cd1bd8bade898e0"
Reward: "0.234696774029 KSM", Date: "12-04-24", Transaction: "0xb8a4e92c2d229fec44d8504787e3231ee6734c5b674cde22eb4d38a08169acb0"
Reward: "0.209174410238 KSM", Date: "11-04-24", Transaction: "0x068f12927126eeb6c146f249d45dcc7d17fbc96381cd3496132c2af087087bb8"
Reward: "0.236433298903 KSM", Date: "11-04-24", Transaction: "0xf2cc81fadb03aba4eae4c0b552bcfa4a86e0f8e9293a0ec1a4d4c1ae57d62b27"
Reward: "0.137144526628 KSM", Date: "11-04-24", Transaction: "0xa4858e339bcc3397c1cb20d08a27f9a264dab4ebde87f5e7d5a94a1219381d15"
Reward: "0.132036418708 KSM", Date: "11-04-24", Transaction: "0x1668128f207faf3aa72a6fe88923873dd69b70ad8b568116b31f5098f23289f7"
Reward: "0.101015762257 KSM", Date: "02-04-24", Transaction: "0xc840524d2d6330c1143cc7b49f0a96dbde639a66695b9887e5bbf55c4d3c56e6"
Reward: "0.053573836054 KSM", Date: "02-04-24", Transaction: "0x3c7830967803c7d87b435838f2abd9522d0327248200ce85b36c4455924551ae"
Reward: "0.124693798142 KSM", Date: "02-04-24", Transaction: "0x9bbff4d2ff16ce98e96fd40ed2dae30619a91fcabd837f6335a649852685d800"
Reward: "0.124755358659 KSM", Date: "01-04-24", Transaction: "0xea059691c0af7346da8b72555d66f338a7be80b15ef6720ea376b73cf1329c60"
Reward: "0.001539399510 KSM", Date: "01-04-24", Transaction: "0xdf9c76d7562a6ed11d9badeca7b2e4ff50ed26951d16012c2fd6c7eba4a360d6"
Reward: "0.175404734587 KSM", Date: "01-04-24", Transaction: "0x4d6bad38e0f6551b386bc0e11ecd1c6d84b656cc7e1735f664bf785c4f2d80fd"
Reward: "0.105196861584 KSM", Date: "01-04-24", Transaction: "0x24370bb79c016a54c33ade4ca488826a2d5ec835322751bc8535dc4e3c5428b9"
Summary: "7.126333577213 KSM"

May 2024:
Reward: "0.404827965013 KSM", Date: "02-05-24", Transaction: "0xb0eb8a82b4cf0caa69e9ad22729a0ae6fdea1101d0fab61cf16b14198cb771db"
Summary: "0.404827965013 KSM"

Summary Year 2024: 8.015623616190 KSM
```
