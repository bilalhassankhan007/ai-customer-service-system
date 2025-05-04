import json
import os

def update_knowledge_base(query, response):
    path = 'data/knowledge_base.json'
    
    # Load existing knowledge base or create a new one
    if os.path.exists(path):
        with open(path, 'r') as f:
            kb = json.load(f)
    else:
        kb = {}

    kb[query] = response  # Update with new info

    # Save updated knowledge base
    with open(path, 'w') as f:
        json.dump(kb, f, indent=4)
