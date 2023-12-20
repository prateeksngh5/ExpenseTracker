from expense import Expense

def summarize_expense(expense_file_path):
    expenses : list[Expense] = [] # list of Expense objects
    with open(expense_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(',') # unpacking the tuple
            line_expense = Expense(expense_name, expense_category, float(expense_amount))
            expenses.append(line_expense)
    
    ### finding the total amounts by category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key not in amount_by_category:
            amount_by_category[key] = expense.amount
        else:
            amount_by_category[key] += expense.amount
    
    print("📈 Expense by Category:")
    for key, value in amount_by_category.items():
        print(f"    Category: {key} | Amount: {value}")
    
    ### finding the total amount as whole
    total_expense = 0
    for expense in expenses:
        total_expense += expense.amount
    
    print(f"🔥 Total expense: {total_expense}")
