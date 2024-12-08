import socket

def start_client(server_host='127.0.0.1', server_port=65432):
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Attempt to connect to the server
    try:
        client_socket.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}")
    except ConnectionRefusedError:
        print(f"Connection refused. Is the server running at {server_host}:{server_port}?")
        return
    except socket.error as e:
        print(f"Socket error: {e}")
        return

    # Send a test message to the server
    message = "Hello, server!"
    try:
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent to server: {message}")

        # Wait for response
        response = client_socket.recv(1024)
        if response:
            print(f"Received from server: {response.decode('utf-8')}")
        else:
            print("No response received from server.")

    except socket.error as e:
        print(f"Error communicating with server: {e}")
    finally:
        # Close connection gracefully
        client_socket.close()
        print("Client disconnected cleanly.")

if __name__ == "__main__":
    start_client()