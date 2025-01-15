import json
import requests
import sys


if len(sys.argv) == 2:
    try:
        amount = float(sys.argv[1])
    except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)
import requests

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = r.json()
    price_per = data["bpi"]["USD"]["rate_float"]
    total_price = price_per * amount
    print(f"${total_price:,.4f}")

except requests.RequestException:
    print("Error")
    sys.exit(1)
