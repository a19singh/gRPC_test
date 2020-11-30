import grpc
import details_pb2
import details_pb2_grpc
import Details
from concurrent import futures
import time

host = "127.0.0.1"
port = "12345"
addr = host+':'+port

class ArrayDetailsServicer(details_pb2_grpc.ArrayDetailsServicer):
    def Personal(self, request, context):
        response = details_pb2_grpc.ArrayDetails()
        response.details = Details.Entry(request.Name, request.age)
        yield response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

details_pb2_grpc.add_ArrayDetailsServicer_to_server(ArrayDetailsServicer(), server)
print('Starting server, Listening at port 12345')
server.add_insecure_port(addr)
server.start()

try:
    while True:
        time.sleep(84600)
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    server.stop(0)
