from flask import Flask, render_template

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.

    Parameters:
    - celsius: Temperature in Celsius.

    Returns:
    - float: Temperature in Fahrenheit.
    """
    return celsius * 9 / 5 + 32


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/celsius_to_fahrenheit/<celsius_str>')
def convert_celsius_to_fahrenheit(celsius_str):
    try:
        celsius = float(celsius_str)
        fahrenheit = celsius_to_fahrenheit(celsius)
        return render_template('temperature_conversion.html', celsius=celsius, fahrenheit=fahrenheit)
    except ValueError:
        return "Invalid input. Please enter a valid Celsius value."


if __name__ == '__main__':
    app.run(debug=True)
