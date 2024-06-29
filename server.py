import http.server
import socketserver

# Define the handler class
class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Override the log_message method to suppress log messages
    def log_message(self, format, *args):
        return

# Set the port number
PORT = 8080

# Create a socket server with the specified port and handler
with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print("Server started on port", PORT)
    # Serve HTTP requests indefinitely
    httpd.serve_forever()
