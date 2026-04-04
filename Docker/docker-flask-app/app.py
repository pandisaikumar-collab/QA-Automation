from flask import Flask

app = Flask(__name__)

def process_list():
    numbers = [5, 2, 9, 1, 7]
    numbers.sort()
    return numbers, max(numbers)

@app.route('/')
def home():
    sorted_list, max_val = process_list()
    return f"Sorted: {sorted_list}, Max: {max_val}"

app.run(host='0.0.0.0', port=5000)