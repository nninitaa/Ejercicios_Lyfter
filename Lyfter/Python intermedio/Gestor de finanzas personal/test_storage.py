import pytest
import storage 
from logic import FinanceManager
from models import Transaction

def test_storage_data_creates_files(tmp_path):
    storage.base_data_file = tmp_path / "test_data.json"

    categories = ["Food"]
    transactions = [Transaction("Expense", "Food", 300, "Galletas")]
    
    storage.storage_data(categories, transactions)
    assert storage.base_data_file.exists()

def test_storage_and_load_categories_file_not_exists(tmp_path):
    storage.base_data_file = tmp_path / "no_file.json"

    categories, transactions = storage.load_data()
    assert categories == []
    assert transactions == []

def test_storage_and_load_data_restores_correctly(tmp_path):
    storage.base_data_file = tmp_path / "restore_data.json"
    
    original_categories = ["Salario"]
    original_transactions = [Transaction("Income", "Salario", 1500.0, "Clases de ingles")]
    
    storage.storage_data(original_categories, original_transactions)
    loaded_categories, loaded_transactions = storage.load_data()
    
    assert loaded_categories == original_categories
    assert len(loaded_transactions) == 1
    assert loaded_transactions[0].title == "Clases de ingles" 

def test_register_transaction_negative_amount():
    manager = FinanceManager()
    manager.categories = ["Food"]
    success, message = manager.register_transaction("Expense", "Food", "-50.0", "Cena")
    
    assert success is False
    assert "amount must be more than 0" in message.lower()