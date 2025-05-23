from src.processing import filter_by_state, sort_by_date

sample_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Пример использования:
filtered_executed = filter_by_state(sample_data)
print(filtered_executed)
# Ожидаемый результат:
# [
#   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
# ]

filtered_canceled = filter_by_state(sample_data, "CANCELED")
print(filtered_canceled)
# Ожидаемый результат:
# [
#   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
# ]

# Пример использования:
sorted_data_desc = sort_by_date(sample_data)
print(sorted_data_desc)
# Ожидаемый результат (сортировка по убыванию даты):
# [
#   {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
#   {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
#   {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
#   {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
# ]
