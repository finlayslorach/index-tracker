from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # To handle Cross-Origin Resource Sharing

# Save cells in a set for simplicity. In production, use a database.
colored_cells = set()

# loading page 
@app.route('/')
def home():
    return render_template('home.html')

# Save which cells are clicked and write to static text file 
@app.route('/save_cell', methods=['POST'])
def save_cell():
    if request.is_json:
        content = request.get_json()
        # Save to database code here
        with open('cells.txt', 'a') as f:
            f.write(content['cell'] + '\n')
        return '', 204
    else:
        return 'Unsupported Media Type', 415

# load saved cells from static text file
@app.route('/get_cells', methods=['GET'])
def get_cells():
    try:
        with open('cells.txt', 'r') as file:
            cells = [line.strip() for line in file]
        return jsonify(cells=cells)
    except FileNotFoundError:
        # If the file doesn't exist yet, just return an empty list.
        return jsonify(cells=[])
    
# # clear saved cells from static text file
@app.route('/reset_cells', methods=['POST'])
def clear_cells():
    if request.is_json:
        content = request.get_json()
        print(content)
        try:
            if content['reset'] == True:
                with open('cells.txt', 'w') as file:
                    file.write('')
                return '', 204
        except FileNotFoundError:
            pass
    return jsonify(cells=[])

if __name__ == '__main__':
    # Load cells from file
    try:
        with open('cells.txt', 'r') as f:
            for line in f:
                colored_cells.add(line.strip())
    except FileNotFoundError:
        pass  # It's OK if the file doesn't exist
    app.run(debug=True)

