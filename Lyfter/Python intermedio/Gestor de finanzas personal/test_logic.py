import logic 

def test_register_category_success(monkeypatch):
    monkeypatch.setattr(logic.storage, 'storage_data', lambda c, t: None)
    logic.categories.clear()
    success, message = logic.register_category("Food")

    assert success is True
    assert "Food" in logic.categories

def test_register_category_empty():
    success, message = logic.register_category("")

    assert success is False
    assert message == "Name category must not be empty"

def test_register_transaction_success(monkeypatch):
    monkeypatch.setattr(logic.storage, 'storage_data', lambda c, t: None)

    logic.categories.clear()
    logic.transaction.clear()

    logic.categories.append("Food")

    success, message = logic.register_transaction(
        "Expense",
        "Food",
        "230"
    )

    assert success is True
    assert len(logic.transaction) == 1