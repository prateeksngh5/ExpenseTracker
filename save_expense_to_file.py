from expense import Expense

def save_expense_to_file(expense, expense_file_path):
    print(f"🎯 Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, 'a') as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
