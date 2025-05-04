from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)

# Define the path to your data directory
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        query = request.form['query']
        response = request.form['response']
        # Here you would typically update your knowledge base or perform other actions
        print(f"Received query: {query}, response: {response}")
        return redirect('/')  # Redirect back to the homepage after submission

    # Handle GET request
    escalated_calls = pd.read_csv(os.path.join(DATA_DIR, 'escalated_calls.csv')).to_dict(orient='records')
    
    return render_template('dashboard.html', escalated_calls=escalated_calls)

if __name__ == '__main__':
    app.run(debug=True)
