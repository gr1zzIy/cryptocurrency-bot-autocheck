import requests
from json import loads

def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")

    #with open("info.txt", "w") as file:
    #    file.write(response.text)

    return response.text

def get_ticker(coin1="btc", coin2="usd"):
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")

    with open("ticker.txt", "w") as file:
        file.write(response.text)

    return response.text

def get_avg(coin="btc"):
    resp = get_ticker(coin)
    as_dict = loads(resp)
    avg = as_dict[f'{coin}_usd']['avg']

    return str(float('{:.2f}'.format(avg))) + "$"

def get_high(coin="btc"):
    resp = get_ticker(coin)
    as_dict = loads(resp)
    high = as_dict[f'{coin}_usd']['high']

    return str(float('{:.2f}'.format(high))) + "$"

def get_low(coin="btc"):
    resp = get_ticker(coin)
    as_dict = loads(resp)
    low = as_dict[f'{coin}_usd']['low']

    return str(float('{:.2f}'.format(low))) + "$"

def get_last(coin="btc"):
    resp = get_ticker(coin)
    as_dict = loads(resp)
    last = as_dict[f'{coin}_usd']['last']

    return str(float('{:.2f}'.format(last))) + "$"

def main():
    #get_info()
    print(get_avg())

if __name__ == "__main__":
    main()