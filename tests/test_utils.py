import pytest
from utils import get_data
from utils import get_filtered_data, get_last_values, get_formated_data


def test_get_data():
    """ Тестирование получения данных"""
    data = get_data()
    assert isinstance(data, list)


def test_filtered_data(test_data):
    """ Тестирование фильтрации данных"""
    assert len(get_filtered_data(test_data)) == 3
    assert len(get_filtered_data(test_data)) == 3


def test_get_last_values(test_data):
    """ Тестирование получения данных по дате"""
    data = get_last_values(test_data, 2)
    assert [x['date'] for x in data] == ["2019-08-26T10:50:58.294041", "2019-07-03T18:35:29.512364"]


def test_get_formated_data(test_data):
    """ Тестирование форматирования данных"""
    data = get_formated_data(test_data[:1])
    assert data[0] == "\n26.08.2019 Перевод организации \nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."
    data = get_formated_data(test_data[1:2])
    assert data[0] == "\n03.07.2019 Перевод организации \nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD"
