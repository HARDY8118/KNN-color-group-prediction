Detect HTML color group using K Nearest Neighbours as displayed in [HTML Color Groups](https://www.w3schools.com/colors/colors_groups.asp)

# Tensorflow function

Algorithm tensor can be found in `backend/prediction.ipynb`.

## Installation

Follow guide [Install TensorFlow with pip](https://www.tensorflow.org/install/pip)

# Web app

Web app for above algorithm is developed with gRPC backend and svelte frontend and is driven via envoy proxy.

## Software requirements

- python
- docker
- pip
- protoc
- node.js

## Setup generation

Install backend dependancies
```bash
pip install grpcio-tools
pip install tensorflow
```

Generate python proto code
```bash
python -m grpc_tools.protoc -I./protos --python_out=./backend --grpc_python_out=./backend ./protos/colors.proto
```

Generate javascript proto code
```bash
protoc -I=protos colors.proto --js_out=import_style=commonjs:frontend/lib
```

```bash
protoc -I=protos colors.proto --grpc-web_out=import_style=commonjs,mode=grpcwebtext:frontend/lib
```

Build frontend
```bash
cd frontend
yarn install
yarn build

# For building client code, not using any frameworks
# Frameworks like react, svelte can use proto buffer javascript files directly
# yarn webpack ./client.js --output-path ./public/ --mode development
```

Check if tcp connection is open
```bash
nc -vz 0.0.0.0 50051
```

## Start server

```bash
docker-compose up --build --detach
```
This will start python gRPC server and envoy proxy.

```bash
cd frontend
yarn dev
```
For starting frontend development server.