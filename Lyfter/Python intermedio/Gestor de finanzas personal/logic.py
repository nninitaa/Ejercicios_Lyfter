from models import Transaction, Category
import storage 

categories, transaction = storage.load_data()

def get_categories():
    return categories

def get_transaction_tables():
    return [[t.type, t.category, f"${t.amount:.2f}"] for t in transaction]

def register_category(name: str):
    name = name.strip()
    if not name:
        return False, "Name category must not be empty"
    if name in categories:
        return False, "Category already exists"
    
    categories.append(name)
    storage.storage_data(categories, transaction)
    return True, f"Category '{name}' added"

def register_transaction(type: str, category: str, amount_str: str):
    if not categories:
        return False, "Error: Must create at least one category before adding an expense/income"
    
    try:
        amount = float(amount_str)
        if amount <= 0:
            return False, "Error: Amount must be more than 0"
    except ValueError:
        return False, "Error: Amount must be a valid number"
    
    new_transaction = Transaction(type, category, amount)
    transaction.append(new_transaction)
    storage.storage_data(categories, transaction)
    return True, "Transaction registered successfully"
