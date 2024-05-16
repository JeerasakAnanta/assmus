from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Define route to handle API requests
@app.route('/api/update_scene', methods=['POST'])
def update_scene():
    # Parse JSON data from the request
    data = request.json

    # Extract data from JSON
    # Example: left_box_position = data['left_box_position']

    # Perform actions based on the data received
    # Example: Update scene based on the received position data Set 
    # Return a response (if necessary)
    return jsonify({'message': 'Scene updated successfully'})

if __name__ == '__main__':
    app.run(debug=True)
