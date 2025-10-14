import matplotlib.pyplot as plt

def plot_budget_distribution(budget_data):
    labels = [item['category'] for item in budget_data['budgets']]
    sizes = [item['amount'] for item in budget_data['budgets']]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title('Budget Distribution')
    return fig

def plot_expense_breakdown(expense_data):
    labels = [item['expense'] for item in expense_data['expenses']]
    sizes = [item['amount'] for item in expense_data['expenses']]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(labels, sizes, color='skyblue')
    plt.title('Expense Breakdown')
    plt.xlabel('Expenses')
    plt.ylabel('Amount')
    plt.xticks(rotation=45)
    return fig