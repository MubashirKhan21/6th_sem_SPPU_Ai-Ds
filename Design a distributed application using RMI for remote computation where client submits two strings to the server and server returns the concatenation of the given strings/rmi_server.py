import Pyro5.api

# Define the remote class
@Pyro5.api.expose
class StringConcatenation:
    def concatenate(self, str1, str2):
        return str1 + str2

# Start the Pyro5 server
def main():
    daemon = Pyro5.api.Daemon()  # Create a server daemon
    ns = Pyro5.api.locate_ns()  # Locate the Pyro5 nameserver
    uri = daemon.register(StringConcatenation)  # Register the remote object
    ns.register("string.concat", uri)  # Register with a unique name

    print("✅ RMI Server is running and waiting for requests...")
    daemon.requestLoop()  # Keep server running

if __name__ == "__main__":
    main()
