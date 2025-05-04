import json
from utils import log_call
from knowledge_base_manager import update_knowledge_base
import os
import datetime

ESCALATIONS_PATH = 'data/escalated_calls.json'

class AIAgent:
    def __init__(self):
        self.load_knowledge_base()
        self.escalated_queries = set()
        self.ensure_escalation_file()

    def ensure_escalation_file(self):
        if not os.path.exists(ESCALATIONS_PATH):
            with open(ESCALATIONS_PATH, 'w') as f:
                json.dump({}, f)

    def load_knowledge_base(self):
        with open('data/knowledge_base.json') as f:
            self.knowledge_base = json.load(f)

#    def save_and_reload_knowledge_base(self, query, supervisor_response):
#        update_knowledge_base(query, supervisor_response)
#        self.load_knowledge_base()
#        print("AI: Knowledge base updated and reloaded.")
#        self.remove_escalation(query)
    def save_and_reload_knowledge_base(self, query, supervisor_response):
        update_knowledge_base(query, supervisor_response)
        self.load_knowledge_base()
        print("AI: Knowledge base updated and reloaded.")
        #self.resolve_escalation(query)
    def respond_to_query(self, query):
        for key in self.knowledge_base:
            if key.lower() in query.lower():
                return self.knowledge_base[key]
        return None

    def escalate_to_supervisor(self, query):
        if query in self.escalated_queries:
            print("AI: I have already escalated this query. Please check the supervisor's response.")
            return

        print(f"Escalating query: {query}")
        self.escalated_queries.add(query)
        self.add_escalation(query)
        supervisor_response = input("Supervisor: Please provide an answer (or press Enter to skip): ")
        #supervisor_response = input("Supervisor: Please provide an answer: ")
        self.handle_supervisor_response(query, supervisor_response)

    def handle_supervisor_response(self, query, supervisor_response):
        print("AI: Thank you! Updating my knowledge base...")
        self.save_and_reload_knowledge_base(query, supervisor_response)
        #########
        if supervisor_response.strip():  # Check if the response is not empty
            self.resolve_escalation(query)
        else:
            print("AI: No response provided by the supervisor. Escalation remains pending.")
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_call(current_time, "1", query, supervisor_response, "Yes")

    def add_escalation(self, query):
        with open(ESCALATIONS_PATH, 'r') as f:
            data = json.load(f)
        data[query] = "Pending"
        with open(ESCALATIONS_PATH, 'w') as f:
            json.dump(data, f, indent=4)

#    def remove_escalation(self, query):
#        with open(ESCALATIONS_PATH, 'r') as f:
#            data = json.load(f)
#        if query in data:
#            del data[query]
#            with open(ESCALATIONS_PATH, 'w') as f:
#                json.dump(data, f, indent=4)
    def resolve_escalation(self, query):
        with open(ESCALATIONS_PATH, 'r') as f:
            data = json.load(f)
        if query in data:
            data[query] = "Resolved"
        with open(ESCALATIONS_PATH, 'w') as f:
            json.dump(data, f, indent=4)
    def start(self):
        while True:
            try:
                query = input("Customer: ")
                response = self.respond_to_query(query)
                if response:
                    print(f"AI: {response}")
                    #log_call("2023-10-01 10:15:00", "1", query, response, "No")
                else:
                    self.escalate_to_supervisor(query)
            except EOFError:
                print("\nNo more input. Exiting the program.")
                break
