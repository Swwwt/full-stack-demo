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
        # change <password> to your password
        client = MongoClient('mongodb+srv://Swt:<password>@cluster0-kxxhm.azure.mongodb.net/test?retryWrites=true&w=majority')
        self.db = client.database
        self.db.user.delete_many({})
        self.db.application.delete_many({})

        users = [
            [1, 'swt', 21, 'FEMALE'],
            [2, 'hm', 22, 'MALE'],
        ]
        for user in users:
            self.db.user.insert_one({
                'id': user[0],
                'name': user[1],
                'age': user[2],
                'gender': user[3],
            })
        # print(self.db.users.find_one({'name': 'swt'}))
        # print(self.db.users.find_one({'name': 'hm'}))

    def CreateApplication(self, request, context):
        # type(request): <class 'myapps_pb2.Application'>
        application = {
            'id': request.id,
            'name': request.name,
            'description': request.description,
            'date': request.date,
            'creator': request.creator
        }
        self.db.application.insert_one(application)
        return myapps_pb2.Application()

    def GetApplication(self, request, context):
        application = self.db.application.find_one({'name': request.name})
        if application == None:
            return myapps_pb2.Application()
        # type(application) = dict
        return myapps_pb2.Application(
            id=application['id'],
            name=application['name'],
            description=application['description'],
            date=application['date'],
            creator=application['creator']
        )

    def GetUser(self, request, context):
        user = self.db.user.find_one({'name': request.name})
        if user == None:
            return myapps_pb2.User()
        return myapps_pb2.User(
            id=user['id'],
            name=user['name'],
            age=user['age'],
            gender=user['gender']
        )

    def DeleteApplication(self, request, context):
        self.db.application.delete_one({'name': request.name})
        return myapps_pb2.Application()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    myapps_pb2_grpc.add_DataServiceServicer_to_server(DataService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
