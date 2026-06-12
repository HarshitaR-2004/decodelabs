from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

# Home page
@app.route('/')
def index():
    total = sum(exp['amount'] for exp in expenses)
    return render_template('index.html', expenses=expenses, total=total)


# Add expense
@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    amount = float(request.form['amount'])   # FIXED

    expense = {
        "id": len(expenses) + 1,
        "title": title,
        "amount": amount
    }

    expenses.append(expense)
    return redirect('/')


# Delete expense (safer POST method)
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    global expenses
    expenses = [exp for exp in expenses if exp['id'] != id]
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)