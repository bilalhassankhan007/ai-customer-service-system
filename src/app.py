from flask import Flask, render_template, request, redirect
import json
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        response = request.form['response']

        # 1. Update knowledge base
        try:
            with open('data/knowledge_base.json', 'r+') as f:
                kb = json.load(f)
                kb[query.lower()] = response
                f.seek(0)
                json.dump(kb, f, indent=4)
                f.truncate()
        except Exception as e:
            print(f"Error updating knowledge base: {e}")

        # 2. Update escalated_calls.csv
        try:
            df = pd.read_csv('data/escalated_calls.csv')
            df.loc[(df['query'] == query) & (df['status'] == 'Pending'), 'status'] = 'Resolved'
            df.to_csv('data/escalated_calls.csv', index=False)
        except Exception as e:
            print(f"Error updating escalated calls: {e}")

        return redirect('/')

    return render_template('dashboard.html')  # Renders the dashboard page

if __name__ == '__main__':
    app.run(debug=True)
