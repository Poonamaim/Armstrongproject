from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello, world'

@app.route('/Armstrong/<int:n>')

def Armstrong(n):
    sum_of_digits = 0
    order = len(str(n))
    copy_n = n

    while n > 0:
        digit = n % 10
        sum_of_digits += digit ** order
        n //= 10  # Use floor division to avoid float results

    if sum_of_digits == copy_n:
        print(f"{copy_n} is an Armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "122.234.213.53",
            "other_details":
            [
                {'id': 1, 'name': 'Alice'},
                {'id': 2, 'name': 'Bob'},
                {'id': 3, 'name': 'poonam'},
                {'id': 4, 'name': 'seema'}

            ]


        }
    else:
        print(f"{copy_n} is not an Armstrong number")
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "122.234.213.53",
            "Other Numbers": [1, 3, 4, 5]
        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)