

################################# Start application
python src/main.py --> chatbot
python app.py --> frontend 


################################ Description

This project is an AI-driven Customer Service System designed to handle customer queries automatically.
It uses a simple knowledge base to answer known questions and escalates unknown queries to a supervisor for manual handling.
Supervisor responses are saved to improve the AI over time.

Main components:
	•	src/ai_agent.py — Core AI agent that interacts with customers.
	•	data/knowledge_base.json — Stores question-answer pairs.
	•	data/call_logs.csv — Logs all customer interactions.
	•	data/escalated_calls.csv — Logs escalated queries.
	•	models/ — Placeholder for future AI model training (optional for smarter responses).
	•	scripts/ — Scripts to run or train the system. You can create and train your AI
	•	tests/ — Unit tests for core functionality.
    •   app.py - Main frontend of this dashboard. You can check and manage easclated call here.

Flow:
	•	Customer asks a question ➔ AI tries to answer ➔ If unknown, escalate to supervisor ➔ Supervisor teaches AI ➔ AI updates its knowledge base.


################################# Directory overview
├── config
├── app.py
├── data
│   ├── call_logs.csv
│   ├── escalated_calls.csv
│   └── knowledge_base.json
├── docs
├── models
│   ├── ai_model.pkl
│   └── training_data.csv
├── README.md
├── scripts
│   ├── run_server.sh
│   └── train_model.sh
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── ai_agent.cpython-313.pyc
│   │   ├── knowledge_base_manager.cpython-313.pyc
│   │   └── utils.cpython-313.pyc
│   ├── ai_agent.py
│   ├── escalation_handler.py
│   ├── knowledge_base_manager.py
│   ├── main.py
│   ├── supervisor_interface.py
│   └── utils.py
└── tests
    └── test_ai_agent.py
