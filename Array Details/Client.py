import grpc
import details_pb2
import details_pb2_grpc
import Details


channel = grpc.insecure_channel('localhost:12345')
stub = details_pb2_grpc.ArrayDetailsStub(channel)
details = details_pb2.Details(Name=input('Enter Name: '),age= int(input('Enter Age: ')) )
response = stub.Personal(details)
print('last line reached')
print(response)