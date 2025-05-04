#!/bin/bash

# Start the server for the supervisor interface
echo "Starting the supervisor interface server..."
# Command to run the server (e.g., using Flask or another framework)
python3 -m flask run --host=0.0.0.0 --port=5000
