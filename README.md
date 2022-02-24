# Colors Guess

Detect HTML color group using K Nearest Neighbours as displayed in [HTML Color Groups](https://www.w3schools.com/colors/colors_groups.asp)

## Tensorflow function

## Web app

## Software requirements

- python
- pip
- protoc

## Proto generation

```bash
pip install grpcio-tools
pip install tensorflow
```

```bash
python -m grpc_tools.protoc -I./protos --python_out=./backend --grpc_python_out=./backend ./protos/colors.proto
```

```bash
protoc -I=. colors.proto --js_out=import_style=commonjs:frontend/lib
```

```bash
protoc -I=. ./protos/colors.proto --grpc-web_out=import_style=commonjs,mode=grpcwebtext:frontend/lib
```

```bash
cd frontend
yarn install
# yarn webpack ./client.js --output-path ./public/ --mode development
```
 nc -vz 0.0.0.0 50051
