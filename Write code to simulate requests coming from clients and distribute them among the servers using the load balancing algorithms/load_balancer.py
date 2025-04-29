import random
import time
import threading

class Server:
    """ Represents a Server handling requests """
    def __init__(self, server_id):
        self.server_id = server_id
        self.active_connections = 0

    def process_request(self, request_id):
        """ Simulate processing a request """
        self.active_connections += 1
        print(f"🔵 Server {self.server_id} processing Request {request_id} (Active: {self.active_connections})")
        time.sleep(random.uniform(1, 3))  # Simulate processing time
        self.active_connections -= 1
        print(f"🟢 Server {self.server_id} finished Request {request_id} (Active: {self.active_connections})")

class LoadBalancer:
    """ Distributes client requests among available servers """
    def __init__(self, servers, algorithm="round_robin"):
        self.servers = servers
        self.algorithm = algorithm
        self.request_count = 0
        self.lock = threading.Lock()

    def distribute_request(self, request_id):
        """ Distribute requests based on the chosen load balancing algorithm """
        with self.lock:
            if self.algorithm == "round_robin":
                selected_server = self.servers[self.request_count % len(self.servers)]
                self.request_count += 1
            elif self.algorithm == "least_connections":
                selected_server = min(self.servers, key=lambda s: s.active_connections)
            elif self.algorithm == "random":
                selected_server = random.choice(self.servers)
            else:
                raise ValueError("Invalid load balancing algorithm!")

        # Process request on the selected server
        threading.Thread(target=selected_server.process_request, args=(request_id,)).start()

def simulate_requests(load_balancer, num_requests=10, delay=0.5):
    """ Simulate multiple client requests """
    for i in range(1, num_requests + 1):
        print(f"\n⚡ Client Request {i} Sent")
        load_balancer.distribute_request(i)
        time.sleep(delay)

if __name__ == "__main__":
    # Create 3 server instances
    servers = [Server(i) for i in range(1, 4)]

    # Choose load balancing algorithm: "round_robin", "least_connections", "random"
    algorithm = "round_robin"  # Change this to test different algorithms

    # Create Load Balancer
    load_balancer = LoadBalancer(servers, algorithm=algorithm)

    # Simulate client requests
    simulate_requests(load_balancer, num_requests=10, delay=1)
