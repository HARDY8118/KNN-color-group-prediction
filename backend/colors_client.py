import grpc
import colors_pb2
import colors_pb2_grpc

import logging

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = colors_pb2_grpc.GrouperStub(channel)
        _ = stub.Guess(colors_pb2.Color(hex='#f0f0f0'))
        print(_)

if __name__=='__main__':
    logging.basicConfig()
    run()
