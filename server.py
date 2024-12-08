import socket

def start_server(host='127.0.0.1', port=65432):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address provided
    try:
        server_socket.bind((host, port))
    except socket.error as e:
        print(f"Error binding server to {host}:{port} - {e}")
        return

# Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept a connection
        try:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")

# Receive data in a loop
            while True:
                data = conn.recv(1024)
                if not data:
                    # No more data means client disconnected
                    print(f"Client {addr} disconnected.")
                    break

                message = data.decode('utf-8')
                print(f"Received from {addr}: {message}")

                # Respond to client
                response_message = f"Server received: {message}"
                conn.sendall(response_message.encode('utf-8'))

            # Close the connection
            conn.close()

        except KeyboardInterrupt:
            print("Server shutdown requested by user.")
            break
        except socket.error as e:
            print(f"Socket error occurred: {e}")
            break

    # Close the server socket
    server_socket.close()
    print("Server stopped.")

if __name__ == "__main__":
    start_server()