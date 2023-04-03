# Python-gRPC-Gateway

```powershell
virtualenv venv
```

```powershell
pip install -r requirements.txt
```

```powershell
python -m grpc_tools.protoc -I ./proto --python_out=./middleware --grpc_python_out=./middleware ./proto/hello.proto
python -m grpc_tools.protoc -I ./proto/helloworld --python_out=./middleware --grpc_python_out=./middleware ./proto/helloworld/hello_world.proto
```


https://github.com/iamrajiv/helloworld-grpc-gateway