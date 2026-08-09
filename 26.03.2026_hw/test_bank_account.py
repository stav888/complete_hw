import pytest
from bank_account import BankAccount


def test_new_account_is_empty():
    assert BankAccount().is_empty()


def test_deposit_increases_balance():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100


def test_withdraw_decreases_balance():
    account = BankAccount(100)
    account.withdraw(40)
    assert account.get_balance() == 60


def test_overdraft_is_rejected():
    with pytest.raises(ValueError):
        BankAccount(10).withdraw(11)


def test_invalid_deposit_is_rejected():
    with pytest.raises(ValueError):
        BankAccount().deposit(0)


def test_invalid_withdrawal_is_rejected():
    with pytest.raises(ValueError):
        BankAccount(10).withdraw(0)
