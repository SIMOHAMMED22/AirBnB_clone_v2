from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def display_python(text):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>')
def display_number(n):
    if isinstance(n, int):
        return f'{n} is a number'


@app.route('/number_template/<int:n>')
def display_number_template(n):
    if isinstance(n, int):
        template = f'<html><body><h1>Number: {n}</h1></body></html>'
        return render_template_string(template)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    if isinstance(n, int):
        result = 'even' if n % 2 == 0 else 'odd'
        template = (
            f'<html><body><h1>'
            f'Number: {n} is {result}'
            f'</h1></body></html>'
        )
        return render_template_string(template)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True,
        ssl_context='adhoc'
    )
