from concurrent import futures
import logging

import grpc
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        print("Received: x=" + request.x + " y=" + request.y)
        return calculator_pb2.AddResponse(result=request.x + request.y)

def serve():
    print('starting server')
    #server = grpc.server(grpc.ThreadPoolExecutor())
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50055')
    server.wait_for_termination()
    server.start()

if __name__ == '__main__':
    logging.basicConfig()
    serve()