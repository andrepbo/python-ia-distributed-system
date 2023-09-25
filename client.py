import socket
import sys
import time

# Client configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 65432        # Port the server is listening on

# Simulated data to send to the AI server
data = '{"input": [0.1, 0.2, 0.3]}'

# Function to display a progress bar


def print_progress_bar(iteration, total, prefix='', suffix='', length=50, fill='█', print_end='\r'):
    percent = ("{:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
    sys.stdout.flush()
    if iteration == total:
        print()


print('Sending data to the AI server:', data)  # Display the sent data

# Create a socket and connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data.encode())

    # Display a progress bar while waiting for the response
    print('Waiting for the AI server response:', end=' ')
    for i in range(101):
        time.sleep(0.1)
        print_progress_bar(i, 100, prefix='Progress:', suffix='Complete')

    # Receive the response from the AI server (simulation)
    response = '{"output": [0.8, 0.9, 1.0]}'

print('\nResponse received from the AI server:')
print(response)  # Display the received response
