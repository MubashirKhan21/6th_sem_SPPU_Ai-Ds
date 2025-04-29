import xmlrpc.client

# Connect to the XML-RPC server
server = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Get user input
num = int(input("Enter a number to compute factorial: "))

# Call the remote function
result = server.factorial(num)

# Display the result
print(f"✅ Factorial of {num} is: {result}")
#python rpc_server.py