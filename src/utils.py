def log_call(timestamp, customer_id, query, response, escalated):
    log_entry = f"{timestamp} | Customer ID: {customer_id} | Query: {query} | Response: {response} | Escalated: {escalated}"
    print("LOG:", log_entry)
