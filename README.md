# Python-gRPC-Gateway

python grpc gateway sample code

virtualenv venv

pip install grpcio grpcio-tools grpcio-reflection googleapis-common-protos
pip install grpc-gateway-protoc-gen-openapiv2
#pip install grpcio-gateway

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

