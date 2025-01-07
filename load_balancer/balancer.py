# from flask import Flask, request, jsonify
# import random

# class LoadBalancer:
#     def __init__(self, servers):
#         self.servers = servers

#     def get_server(self):
#         return random.choice(self.servers)

# app = Flask(__name__)
# load_balancer = LoadBalancer(servers=["http://server1.com", "http://server2.com", "http://server3.com"])

# @app.route('/balance', methods=['GET'])
# def balance():
#     server = load_balancer.get_server()
#     return jsonify({"server": server})

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
import hash_ring

class LoadBalancer:
    def __init__(self, servers):
        self.ring = hash_ring.HashRing(servers)

    def get_server(self, client_ip):
        return self.ring.get_node(client_ip)

app = Flask(__name__)
load_balancer = LoadBalancer(servers=["http://server1.com", "http://server2.com", "http://server3.com"])

@app.route('/balance', methods=['GET'])
def balance():
    client_ip = request.remote_addr
    server = load_balancer.get_server(client_ip)
    return jsonify({"server": server})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)