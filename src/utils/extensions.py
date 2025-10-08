import requests
import json
from src.models.data import keys, URL, notice


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: float):
        if quote == base:
            raise ConvertionException(f'{notice['clon']} {base}.')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'{notice['currency']} {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'{notice['currency']} {quote}.')
        r = requests.get(f'{URL}fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base

    @staticmethod
    def valid_data(input_list: str) -> str:
        # не указываем разделитель split(), чтобы предупредить ошибк пользователя с двумя и более пробелами или табуляцией
        values = input_list.split()
        if len(values) != 3:
            raise ConvertionException(notice['insert'])
        quote, base, amount_str = [s.lower() for s in values]
        try:
            amount = float(amount_str)
        except ValueError:
            raise ConvertionException(f'{notice["amount"]} "{amount_str}" — не число.')
        if amount <= 0:
            raise ConvertionException(notice['value_amount'])
        total_base = CryptoConverter.convert(quote, base, amount)
        # расчеты стоимости одной валюты относительно другой производим с учетом amount - умножением
        text = f'Цена {amount} {quote} в {base} - {float(total_base) * float(amount)}'
        return text
