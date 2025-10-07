import requests
from src.utils.data import URL

def get_price(from_symbol: str, to_symbol: str) -> float:
    url = URL
    params = {"fsym": from_symbol.upper(), "tsyms": to_symbol.upper()}
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    if "Error" in data:
        raise ValueError(data["Error"])
    return data[to_symbol.upper()]