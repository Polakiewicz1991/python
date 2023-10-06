import requests

coinsList = None

def getCoinsList():
    global coinsList
    # {'id': '01coin', 'symbol': 'zoc', 'name': '01coin'}
    response = requests.get("https://api.coingecko.com/api/v3/coins/list")
    if response.ok == True:
        print("response OK")
        data = response.json()
        print("response data lenght: ", len(data))
        print("1st sample: ",data[0])

        coinsList = data
    else:
        print("response nOK")


def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    if coinsList is not None:
        for coin in coinsList:
            if coin["symbol"] == symbol:
                return coin
        else:
            return None
    else:
        print("nie udało się")
        return None
getCoinsList()

btcData = findCoinBySymbol("btc")
print(btcData)