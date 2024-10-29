from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_random_color():
    # Generate a random HEX color code
    hex_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    return hex_color

@app.route('/random-color', methods=['GET'])
def random_color():
    # Return the generated random color as a JSON response
    color = generate_random_color()
    return jsonify({"color": color})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
