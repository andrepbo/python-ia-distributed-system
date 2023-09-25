import socket
import sys
import time
import json
import numpy as np  # We'll use NumPy to simulate AI processing

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Port the server will listen on

# Function to simulate AI processing


def simulate_ai_processing(input_data):
    # Here we are just adding a fixed value to each element of the input data
    processed_data = [x + 0.5 for x in input_data]
    return processed_data


# Initialize the socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print('Waiting for connections...')

    conn, addr = s.accept()
    print('Connection established by', addr)

    with conn:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break

            print('Data received:', data)

            # Convert the received data to a usable format (JSON)
            input_data = json.loads(data)['input']

            # Simulate AI processing
            processed_data = simulate_ai_processing(input_data)

            # Prepare the response
            response = {'output': processed_data}
            response_json = json.dumps(response)

            # Send the response back to the client
            conn.sendall(response_json.encode())

            print('Response sent:', response_json)
