import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc
import grpc_gateway

class CalculatorGateway(grpc_gateway.GatewayServicer):
    def Add(self, request):
        channel = grpc.insecure_channel('localhost:50055')
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(x=request['x'], y=request['y']))
        return {'result': response.result}

gateway = grpc_gateway.Gateway([CalculatorGateway()], 'localhost:8080')
gateway.run()