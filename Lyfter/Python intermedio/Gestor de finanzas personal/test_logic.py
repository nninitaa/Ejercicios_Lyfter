import pytest
from logic import FinanceManager 

def test_register_category_success(monkeypatch):
    manager = FinanceManager()
    monkeypatch.setattr("storage.storage_data", lambda c, t: None)
    manager.categories.clear()
    success, message = manager.register_category("Food")
    
    assert success is True
    assert "Food" in manager.categories


def test_register_category_empty():
    manager = FinanceManager()
    success, message = manager.register_category("")

    assert success is False
    assert message == "Name category must not be empty"


def test_register_transaction_success(monkeypatch):
    manager = FinanceManager()
    monkeypatch.setattr("storage.storage_data", lambda c, t: None)
    manager.categories.clear()
    manager.transactions.clear()
    manager.categories.append("Food")
    success, message = manager.register_transaction(
        "Expense",
        "Food",
        "230",
        "Galletas" 
    )

    assert success is True
    assert len(manager.transactions) == 1
    assert manager.transactions[0].title == "Galletas"


def test_register_transaction_empty_title(monkeypatch):
    manager = FinanceManager()
    monkeypatch.setattr("storage.storage_data", lambda c, t: None)
    manager.categories.clear()
    manager.categories.append("Food")
    success, message = manager.register_transaction("Expense", "Food", "100", "   ")
    
    assert success is False
    assert "title must not be empty" in message.lower()


def test_register_transaction_empty_category(monkeypatch):
    manager = FinanceManager()
    monkeypatch.setattr("storage.storage_data", lambda c, t: None)
    manager.categories.clear()
    manager.categories.append("Food") 
    success, message = manager.register_transaction("Expense", "", "230", "Galletas")

    assert success is False
    assert "please select a category" in message.lower()