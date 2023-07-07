from src.utils import check_valid_operation


def test_check_valid_operation():
    assert check_valid_operation({'date': 1, 'state': 'EXECUTED', 'description': 1}) is True
    assert check_valid_operation({'state': 'EXECUTED', 'description': 1}) is None
    assert check_valid_operation({'date': 1, 'state': 'EXECU', 'description': 1}) is False
    assert check_valid_operation({'date': 1, 'state': 'EXECUTED', 'description': 'Открытие вклада'}) is False
