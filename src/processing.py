from datetime import datetime
from typing import Dict, List


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по заданному состоянию (state).

    :param data: Список словарей с данными об операциях.
    :param state: Состояние, по которому нужно сделать фильтрацию.
                  По умолчанию 'EXECUTED'.
    :return: Новый список, содержащий только те словари, у которых
             значение по ключу 'state' соответствует указанному параметру.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список операций по ключу 'date'.

    :param data: Список словарей с данными об операциях.
    :param reverse: Порядок сортировки:
                    True — по убыванию (сначала самые новые),
                    False — по возрастанию.
                    По умолчанию True.
    :return: Новый список, отсортированный по дате.
    """
    # Преобразуем дату к объекту datetime, чтобы корректно отсортировать
    return sorted(data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=reverse)
