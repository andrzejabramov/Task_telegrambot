import requests
import json
from loguru import logger
from src.models.data import keys, URL, notice


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: float):
        logger.debug(f"Запрос конвертации: {amount} {quote} → {base}")
        if quote == base:
            err_msg = f'{notice["clon"]} {base}.'
            logger.warning(f"Попытка конвертации валюты в саму себя: {quote}")
            raise ConvertionException(err_msg)
        if base not in keys:
            err_msg = f'{notice["currency"]} {base}.'
            logger.warning(f"Неизвестная базовая валюта: {base}")
            raise ConvertionException(err_msg)
        if quote not in keys:
            err_msg = f'{notice["currency"]} {quote}.'
            logger.warning(f"Неизвестная котируемая валюта: {quote}")
            raise ConvertionException(err_msg)
        try:
            url = f'{URL}fsym={keys[quote]}&tsyms={keys[base]}'
            logger.debug(f"Запрос к API: {url}")
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            data = r.json()
            rate = data[keys[base]]
            logger.debug(f"Получен курс: 1 {quote} = {rate} {base}")
            return rate
        except requests.RequestException as e:
            logger.error(f"Ошибка при запросе к API: {e}")
            raise ConvertionException("Не удалось получить данные от сервера курсов валют.")

    @staticmethod
    def valid_data(input_list: str) -> str:
        logger.debug(f"Валидация входных данных: {input_list!r}")
        values = input_list.split()
        if len(values) != 3:
            err_msg = notice['insert']
            logger.warning(f"Неверное количество аргументов: {len(values)} вместо 3. Ввод: {input_list!r}")
            raise ConvertionException(err_msg)
        quote, base, amount_str = [s.lower() for s in values]
        try:
            amount = float(amount_str)
        except ValueError:
            err_msg = f'{notice["amount"]} "{amount_str}" — не число.'
            logger.warning(f"Некорректная сумма: {amount_str!r}")
            raise ConvertionException(err_msg)

        if amount <= 0:
            err_msg = notice['value_amount']
            logger.warning(f"Сумма <= 0: {amount}")
            raise ConvertionException(err_msg)

        rate = CryptoConverter.convert(quote, base, amount)
        result = rate * amount
        result_text = f'Цена {amount} {quote} в {base} - {result:.6f}'
        logger.info(f"Результат расчёта: {result_text}")
        return result_text
