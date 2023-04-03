from concurrent import futures
import logging
import grpc
import hello_pb2
import hello_pb2_grpc

class Hellos(hello_pb2_grpc.HellosServicer):

    def GetHello(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        print("Received:" + request.name)
        return hello_pb2.HelloResponse(msg=request.name, name=request.name)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HellosServicer_to_server(Hellos(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()
    print("Hello Server started!")

if __name__ == '__main__':
    logging.basicConfig()
    serve()