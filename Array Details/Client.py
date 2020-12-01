import grpc
import details_pb2
import details_pb2_grpc
import Details

host = "127.0.0.1"
port = "12345"
addr = host+':'+port

channel = grpc.insecure_channel(addr)
stub = details_pb2_grpc.ArrayDetailsStub(channel)
details = details_pb2.Details(Name=input('Enter Name: '),age= int(input('Enter Age: ')) )

response = stub.Personal(details)
print('last line reached')
try:
    print(response.result())
except:
    print("[ - ] Unable to get result.")
    print(response.details())
