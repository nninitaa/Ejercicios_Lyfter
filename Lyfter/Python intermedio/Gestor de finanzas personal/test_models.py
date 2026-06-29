from models import Category, Transaction

def test_category_name_trim():
    category = Category("  Food  ")
    assert category.name == "Food"

def test_transaction_creation():
    transaction = Transaction("Expense", "Food", 230)
    assert transaction.type == "Expense"
    assert transaction.category == "Food"
    assert transaction.amount == 230.0

def test_transaction_amount_float():
    transaction = Transaction("Income", "Salary", "1500")
    assert isinstance(transaction.amount, float)
    assert transaction.amount == 1500.0

