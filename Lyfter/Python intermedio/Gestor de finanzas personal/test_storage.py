import storage 
from models import Transaction

def test_storage_data_creates_files(tmp_path):
    storage.base_data_file = tmp_path / "test_data.json"

    categories = ["Food"]
    transactions = [Transaction("Expenses", "Food", 300)]
    storage.storage_data(categories, transactions)
    assert storage.base_data_file.exists()

def test_storage_and_load_categories(tmp_path):
    storage.base_data_file = tmp_path / "no_file.json"

    categories, transactions = storage.load_data()

    categories = []
    transactions = []