from concurrent import futures
from pymongo import MongoClient
from random import randint
import logging

import grpc

import myapps_pb2
import myapps_pb2_grpc

from google.protobuf.timestamp_pb2 import Timestamp


class DataService(myapps_pb2_grpc.DataServiceServicer):

    def __init__(self):
        client = MongoClient('mongodb+srv://Swt:Swt980803@cluster0-kxxhm.azure.mongodb.net/test?retryWrites=true&w=majority')
        self.db = client.database
        print(self.db.user.find_one({'name': 'swt'}))
        print(self.db.user.find_one({'name': 'hm'}))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    myapps_pb2_grpc.add_DataServiceServicer_to_server(DataService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
