import grpc
import colors_pb2
import colors_pb2_grpc
from concurrent import futures
import logging
import sys

from knn_predictor import KNN_Predictor

knn = KNN_Predictor()
if not knn.load_csv('colors.csv',True):
    print("Failed to load data")
    sys.exit(1)

print("Data loaded successfully")


class GrouperServicer(colors_pb2_grpc.GrouperServicer):
    # def __init__(this):
    #     pass
    # def Guess(this, request, context):
    #     return colors_pb2.Group(group="Success")
    def Guess(this, request, context):
        return colors_pb2.Group(group=knn.predic(request.hex))
    

def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    colors_pb2_grpc.add_GrouperServicer_to_server(GrouperServicer(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__=='__main__':
    print('Starting server')
    logging.basicConfig()
    serve()
