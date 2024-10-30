from flask import Flask, jsonify
import random
import awsgi

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

# AWS Lambda handler
def lambda_handler(event, context):
    # Use awsgi to handle the Lambda event and send it to the Flask app
    return awsgi.response(app, event, context)
