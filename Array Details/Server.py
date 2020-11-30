import grpc
import details_pb2
import details_pb2_grpc
import Details
from concurrent import futures
import time

class ArrayDetailsServicer(details_pb2_grpc.ArrayDetailsServicer):
    def Personal(self, request, context):
        response = details_pb2_grpc.ArrayDetails()
        response.details = Details.Entry(request.Name, request.age)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

details_pb2_grpc.add_ArrayDetailsServicer_to_server(ArrayDetailsServicer(), server)
print('Starting server, Listening at port 12345')
server.add_insecure_port('[::]:12345')
server.start()

try:
    while True:
        time.sleep(84600)
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    server.stop(0)

