# Expense Class: Has three attributes namely, Expense Name, Expense Category and Expense Amount
class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return f"<Expense: {self.name}, {self.category}, {self.amount}>"
