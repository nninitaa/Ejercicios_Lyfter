from models import Transaction, Category
import storage 

class FinanceManager:
    def __init__(self):
        self.categories, self.transactions = storage.load_data()

    def get_categories(self):
        return self.categories

    def get_transaction_tables(self):
        return [[t.title, t.type, t.category, f"${t.amount:.2f}"] for t in self.transactions]

    def register_category(self, name: str):
        name = name.strip()
        if not name:
            return False, "Name category must not be empty"
        if name in self.categories:
            return False, "Category already exists"
        
        self.categories.append(name)
        storage.storage_data(self.categories, self.transactions)
        return True, f"Category '{name}' added"

    def register_transaction(self, transaction_type: str, category: str, amount_str: str, title: str):
        if not self.categories:
            return False, "Error: Must create at least one category before adding an expense/income"
        
        title = title.strip()
        if not title:
            return False, "Error: Title must not be empty"
            
        category = category.strip() if category else ""
        if not category:
            return False, "Error: Please select a category"
        
        try:
            amount = float(amount_str)
            if amount <= 0:
                return False, "Error: Amount must be more than 0"
        except ValueError:
            return False, "Error: Amount must be a valid number"
        
        new_transaction = Transaction(transaction_type, category, amount, title)
        self.transactions.append(new_transaction)
        storage.storage_data(self.categories, self.transactions)
        return True, "Transaction registered successfully"
