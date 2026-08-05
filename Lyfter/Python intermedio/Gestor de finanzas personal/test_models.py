from models import Category, Transaction

def test_category_name_trim():
    category = Category("  Food  ")
    assert category.name == "Food"

def test_transaction_creation():
    transaction = Transaction(transaction_type="Expense", category="Food", amount=230.0, title="Galletas")
    assert transaction.type == "Expense"
    assert transaction.category == "Food"
    assert transaction.amount == 230.0
    assert transaction.title == "Galletas" 

def test_transaction_amount_float():
    transaction = Transaction(transaction_type="Income", category="Salary", amount=1500.0, title="Pago mensual")
    assert isinstance(transaction.amount, float)
    assert transaction.amount == 1500.0

def test_transaction_title_assignment():
    transaction = Transaction(transaction_type="Expense", category="Entertainment", amount=15.0, title="Netflix")
    assert transaction.title == "Netflix"

