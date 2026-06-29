class Category:
    def __init__(self, name: str):
        self.name = name.strip()

class Transaction:
    def __init__(self, type: str, category: str, amount: float):
        self.type = type
        self.category = category
        self.amount = float(amount)