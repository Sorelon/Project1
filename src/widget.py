from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Функция принимает строку с типом карты/счета и номер и возвращает строку с замаскированным номером"""
    letters = ""
    digits = ""

    for char in info:  # Разделение букв и цифр из исходной строки
        if char.isdigit():
            digits += char
        elif char.isalpha() or char.isspace():
            letters += char

    letters = letters.rstrip()  # Убираем лишние пробелы в конце строки

    if info.lower().startswith("счет"):  # Определяем, маскировать номер счета или карты
        masked_number = get_mask_account(digits)
    else:
        masked_number = get_mask_card_number(digits)

    return f"{letters} {masked_number}"


def get_date(date_string: str) -> str:
    """
    Преобразует строку с датой в формате "2024-03-11T02:26:18.671407"
    в формат "ДД.ММ.ГГГГ".

    :param date_string: Строка с датой
    в формате "2024-03-11T02:26:18.671407".
    :return: Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    return date_object.strftime("%d.%m.%Y")
