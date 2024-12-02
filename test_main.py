from main import check_balance
import pytest


def test_check_balance_1():
    data = '(((([{}]))))'
    expected = 'Сбалансированно'
    assert check_balance(data) == expected


def test_check_balance_2():
    data = '[([])((([[[]]])))]{()}'
    expected = 'Сбалансированно'
    assert check_balance(data) == expected


def test_check_balance_3():
    data = '{{[()]}}'
    expected = 'Сбалансированно'
    assert check_balance(data) == expected


def test_check_balance_4():
    data = '}{}'
    expected = 'Несбалансированно'
    assert check_balance(data) == expected


def test_check_balance_5():
    data = '{{[(])]}}'
    expected = 'Несбалансированно'
    assert check_balance(data) == expected


def test_check_balance_6():
    data = '[[{())}]'
    expected = 'Несбалансированно'
    assert check_balance(data) == expected
