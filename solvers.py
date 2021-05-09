import requests
from decimal import Decimal

def Solve1():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)

    quoteAssetBTC = []
    for i in response.json():
        if i["symbol"][-3:] == "BTC": 
            quoteAssetBTC.append(i)

    topFiveQuoteAssetBTCwithVolume = []
    for j in sorted(quoteAssetBTC, key = lambda x: x["volume"], reverse = True)[0:5]:
        topFiveQuoteAssetBTCwithVolume.append(dict(symbol=j["symbol"], volume=j["volume"]))

    return topFiveQuoteAssetBTCwithVolume

def Solve2():
    url = "https://api.binance.com/api/v3/ticker/24hr"
    response = requests.get(url)

    quoteAssetUSDT = []
    for i in response.json():
        if i["symbol"][-4:] == "USDT": 
            quoteAssetUSDT.append(i)

    topFiveQuoteAssetUSDTwithTrades = []
    for j in sorted(quoteAssetUSDT, key = lambda x: x["count"], reverse = True)[0:5]:
        topFiveQuoteAssetUSDTwithTrades.append(dict(symbol=j["symbol"], count=j["count"]))

    return topFiveQuoteAssetUSDTwithTrades  

def Solve3():
    symbols = [x["symbol"] for x in Solve1()]

    urls = ["https://api.binance.com/api/v3/depth?symbol={}".format(symbol) for symbol in symbols] 

    symbolValuePair = []
    for url in urls:
        response = requests.get(url)
        sumOfBids = 0
        sumOfAsks = 0

        for i in response.json()["bids"]:
            sumOfBids += (Decimal(i[0]) * Decimal(i[1]))

        for j in response.json()["asks"]:
            sumOfAsks += (Decimal(i[0]) * Decimal(i[1]))    

        symbolValuePair.append(dict(symbol=url[44:], value= sumOfBids + sumOfAsks))

    return symbolValuePair

def Solve4():
    symbols = [x["symbol"] for x in Solve2()]    

    urls = ["https://api.binance.com/api/v3/ticker/bookTicker?symbol={}".format(symbol) for symbol in symbols] 

    symbolSpreadPair = []
    for url in urls:
        response = requests.get(url)

        priceSpread = Decimal(response.json()["askPrice"]) - Decimal(response.json()["bidPrice"])
        symbolSpreadPair.append(dict(symbol=url[56:], spread=priceSpread))

    return symbolSpreadPair    

temp = []
def Solve5():
    while True:
        symbols = [x["symbol"] for x in Solve2()]    
        urls = ["https://api.binance.com/api/v3/ticker/bookTicker?symbol={}".format(symbol) for symbol in symbols] 
        symbolSpreadPair = []

        for url in urls:
            response = requests.get(url)
            priceSpread = Decimal(response.json()["askPrice"]) - Decimal(response.json()["bidPrice"])
            temp.append(priceSpread)
            symbolSpreadPair.append(dict(symbol=url[56:], spread=priceSpread))

        deltaList = [None]*10
        for i in range(len(deltaList)):
            if len(temp) == 5 and i < 5:
                symbolSpreadPair[i]["delta"] = None
            elif len(temp) > 5 and i < 5:
                deltaList = temp[-10:]
                symbolSpreadPair[i]["delta"] = abs(deltaList[i+5] - deltaList[i])

        return symbolSpreadPair
