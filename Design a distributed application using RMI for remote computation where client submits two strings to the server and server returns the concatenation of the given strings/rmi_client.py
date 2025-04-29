import Pyro5.api

# Connect to the remote object
def main():
    ns = Pyro5.api.locate_ns()  # Locate the Pyro5 nameserver
    uri = ns.lookup("string.concat")  # Look up the registered object
    remote_object = Pyro5.api.Proxy(uri)  # Get a proxy for the remote object

    # Get input from user
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    # Call the remote method
    result = remote_object.concatenate(str1, str2)

    print(f"✅ Concatenated Result: {result}")

if __name__ == "__main__":
    main()
