# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import myapps_pb2 as myapps__pb2


class DataServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateApplication = channel.unary_unary(
        '/DataService/CreateApplication',
        request_serializer=myapps__pb2.Application.SerializeToString,
        response_deserializer=myapps__pb2.Application.FromString,
        )
    self.GetApplication = channel.unary_unary(
        '/DataService/GetApplication',
        request_serializer=myapps__pb2.Application.SerializeToString,
        response_deserializer=myapps__pb2.Application.FromString,
        )
    self.GetUser = channel.unary_unary(
        '/DataService/GetUser',
        request_serializer=myapps__pb2.User.SerializeToString,
        response_deserializer=myapps__pb2.User.FromString,
        )
    self.DeleteApplication = channel.unary_unary(
        '/DataService/DeleteApplication',
        request_serializer=myapps__pb2.Application.SerializeToString,
        response_deserializer=myapps__pb2.Application.FromString,
        )


class DataServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateApplication(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetApplication(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUser(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteApplication(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateApplication': grpc.unary_unary_rpc_method_handler(
          servicer.CreateApplication,
          request_deserializer=myapps__pb2.Application.FromString,
          response_serializer=myapps__pb2.Application.SerializeToString,
      ),
      'GetApplication': grpc.unary_unary_rpc_method_handler(
          servicer.GetApplication,
          request_deserializer=myapps__pb2.Application.FromString,
          response_serializer=myapps__pb2.Application.SerializeToString,
      ),
      'GetUser': grpc.unary_unary_rpc_method_handler(
          servicer.GetUser,
          request_deserializer=myapps__pb2.User.FromString,
          response_serializer=myapps__pb2.User.SerializeToString,
      ),
      'DeleteApplication': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteApplication,
          request_deserializer=myapps__pb2.Application.FromString,
          response_serializer=myapps__pb2.Application.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'DataService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))