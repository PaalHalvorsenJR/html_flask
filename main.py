from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Extract numbers and operation from form data
        num1 = request.form.get('num1', type=float)
        num2 = request.form.get('num2', type=float)
        operation = request.form.get('operation')

        # Calculator logic
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Cannot divide by zero'
        else:
            result = 'Invalid operation'

        return render_template('index.html', result=result)

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
