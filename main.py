import grpc
from concurrent import futures
import gen.python.greeter_pb2 as greeter_pb2
import gen.python.greeter_pb2_grpc as greeter_pb2_grpc

class Greeter(greeter_pb2_grpc.GreeterServicer):
    def SayHello(self, request: greeter_pb2.HelloRequest, context):
        return greeter_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    print("Starting server on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
