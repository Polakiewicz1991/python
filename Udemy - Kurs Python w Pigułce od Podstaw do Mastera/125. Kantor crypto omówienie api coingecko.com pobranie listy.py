#https://www.coingecko.com/en/api/documentation

import requests

coinsList = None
currency = 'pln'

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


def getCoinLastMaketData(CoinID = "bitcoin"):
    if CoinID is not None:
        #{'bitcoin': {'pln': 119473, 'pln_market_cap': 2338452805220.1543, 'pln_24h_vol': 62375284222.95747, 'pln_24h_change': -2.541370559386113, 'last_updated_at': 1696598947}}
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={CoinID}&vs_currencies={currency}&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true&precision=true")
        if response.ok == True:
            print("response OK")
            data = response.json()
            return data
        else:
            print("response nOK")
    else:
        print("nie udało się")
        return None

def getCoinPriceInCurrency(CoinID,currency):
    currency = currency.lower().strip()
    marketData = getCoinLastMaketData(CoinID)
    return marketData[CoinID][currency]




getCoinsList()

coinData = findCoinBySymbol("btc")
print(coinData)

marketData = getCoinLastMaketData(coinData['id'])
print(marketData)

coinPrice = getCoinPriceInCurrency(coinData['id'],currency)
print("Na złotówki: ", coinPrice)


print("Kalkulator krypto")

while True:
    cryptoSymbolToBuy = input("Wybierz symbol krypto do kupienia lub wpisz exit, aby zakonczyć:")
    if cryptoSymbolToBuy == "exit": break

    coinData = findCoinBySymbol(cryptoSymbolToBuy)
    if coinPrice == None:
        print("Nie ma takiej waluty")
        continue

    coinPrice = getCoinPriceInCurrency(coinData['id'], currency)
    print(f"{coinData['id']} na złotówki: ", coinPrice)

    moneyToBuyCrypto = float(input("Ile chcesz przeznaczyć na zakup: "))
    boughtCrypto = moneyToBuyCrypto / coinPrice

    print(f"zakupiono {boughtCrypto} {coinData['id']}")