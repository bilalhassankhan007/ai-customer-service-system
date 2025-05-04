from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__, template_folder='src/templates')

KB_PATH = 'data/knowledge_base.json'
ESCALATIONS_PATH = 'data/escalated_calls.json'

# Ensure data files exist
for path in [KB_PATH, ESCALATIONS_PATH]:
    if not os.path.exists(path):
        with open(path, 'w') as f:
            json.dump({}, f)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    # Handle new knowledge base entries
    if request.method == 'POST':
        query = request.form['query']
        response = request.form['response']
        update_knowledge_base(query, response)
        remove_escalation(query)
        return redirect('/')

    # Load escalated queries
    with open(ESCALATIONS_PATH, 'r') as f:
        escalated_data = json.load(f)

    escalated_calls = [{'query': q, 'status': status} for q, status in escalated_data.items()]
    return render_template('dashboard.html', escalated_calls=escalated_calls)

def update_knowledge_base(query, response):
    with open(KB_PATH, 'r') as f:
        kb = json.load(f)
    kb[query] = response
    with open(KB_PATH, 'w') as f:
        json.dump(kb, f, indent=4)

def remove_escalation(query):
    with open(ESCALATIONS_PATH, 'r') as f:
        data = json.load(f)
    if query in data:
        del data[query]
        with open(ESCALATIONS_PATH, 'w') as f:
            json.dump(data, f, indent=4)

if __name__ == '__main__':
    app.run(debug=True)
