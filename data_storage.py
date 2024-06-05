expenses = []

def add_expense(amount, description, category):
    expense = {
        'amount': amount,
        'description': description,
        'category': category
    }
    expenses.append(expense)
    print("Expense added successfully!")
    print()

def get_expenses():
    return expenses
