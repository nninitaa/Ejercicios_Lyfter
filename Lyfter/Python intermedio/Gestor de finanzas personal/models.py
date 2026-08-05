class Category:
    def __init__(self, name: str):
        self.name = name.strip()

class Transaction:
    def __init__(self, transaction_type: str, category: str, amount: float, title: str):
        self.type = transaction_type  
        self.category = category
        self.amount = amount
        self.title = title