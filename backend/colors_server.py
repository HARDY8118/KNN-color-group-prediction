import grpc
import colors_pb2
import colors_pb2_grpc

from concurrent import futures
import logging

class GrouperServicer(colors_pb2_grpc.GrouperServicer):
    # def __init__(this):
    #     pass
    def Guess(this, request, context):
        # TODO
        return colors_pb2.Group(group="Success")

def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    colors_pb2_grpc.add_GrouperServicer_to_server(GrouperServicer(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__=='__main__':
    logging.basicConfig()
    serve()
