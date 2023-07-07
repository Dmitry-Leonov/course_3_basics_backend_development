from src.utils import check_valid_operation, get_executed_operations, operation_masked, get_last_five_operations, \
    get_operations_by_print


def test_check_valid_operation():
    assert check_valid_operation({'date': 1, 'state': 'EXECUTED', 'description': 1}) is True
    assert check_valid_operation({'state': 'EXECUTED', 'description': 1}) is None
    assert check_valid_operation({'date': 1, 'state': 'EXECU', 'description': 1}) is False
    assert check_valid_operation({'date': 1, 'state': 'EXECUTED', 'description': 'Открытие вклада'}) is False


def test_operation_masked():
    assert operation_masked('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert operation_masked('Visa Classic 1596837868705199') == 'Visa Classic 1596 83** **** 5199'
    assert operation_masked('Тип Карты 1111111111111111') == 'Тип Карты 1111 11** **** 1111'
    assert operation_masked('Тип Карты 111111111111111111') == 'Тип Карты 1111 11** **** 1111'
    assert operation_masked('Счет 48894435694657014368') == 'Счет **4368'
    assert operation_masked('Счет 4889443569465701436') == 'Счет 4889 44** **** 1436'


def test_get_executed_operations():
    assert get_executed_operations([
        {'date': 1, 'state': 'EXECUTED', 'description': 1},
        {'date': 1, 'state': 'EXECU', 'description': 1}
    ]) == [{'date': 1, 'state': 'EXECUTED', 'description': 1}]


def test_get_last_five_operations():
    assert get_last_five_operations([
        {'date': 2, 'state': 'EXECUTED', 'description': 1},
        {'date': 5, 'state': 'EXECUTED', 'description': 1},
        {'date': 1, 'state': 'EXECUTED', 'description': 1},
        {'date': 4, 'state': 'EXECUTED', 'description': 1},
        {'date': 3, 'state': 'EXECUTED', 'description': 1},
        {'date': 6, 'state': 'EXECUTED', 'description': 1},

    ]) == [
               {'date': 6, 'state': 'EXECUTED', 'description': 1},
               {'date': 5, 'state': 'EXECUTED', 'description': 1},
               {'date': 4, 'state': 'EXECUTED', 'description': 1},
               {'date': 3, 'state': 'EXECUTED', 'description': 1},
               {'date': 2, 'state': 'EXECUTED', 'description': 1},
           ]


def test_get_operations_by_print():
    assert get_operations_by_print([
        {'date': '2019-07-12T20:41:47.882230', 'from': 'Maestro 1596837868705199', 'to': 'Счет 48894435694657014368',
         'description': 'описание', 'operationAmount': {'amount': '1000', 'currency': {'name': 'USD'}}}
    ]) == [
        {'date': '12.07.2019', 'from': 'Maestro 1596 83** **** 5199', 'to': 'Счет **4368', 'description': 'описание',
         'sum': '1000', 'currency_name': 'USD'}
    ]
