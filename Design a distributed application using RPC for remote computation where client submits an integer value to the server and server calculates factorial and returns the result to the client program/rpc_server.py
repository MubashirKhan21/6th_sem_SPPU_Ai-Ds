from xmlrpc.server import SimpleXMLRPCServer
import math

# Function to calculate factorial
def compute_factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    return str(math.factorial(n))  # Convert to string to avoid integer limits

# Create an XML-RPC server
server = SimpleXMLRPCServer(("localhost", 8000), allow_none=True)
print("✅ XML-RPC Server is running on port 8000...")

# Register the function
server.register_function(compute_factorial, "factorial")

# Keep the server running
server.serve_forever()
#python rpc_client.py