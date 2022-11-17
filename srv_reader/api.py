from flask import Blueprint, request
import grpc
import logging
import retrieve_time_pb2
import retrieve_time_pb2_grpc

logging.basicConfig(filename='apiAccess.log', level=logging.INFO)
blueprintApi = Blueprint('timeAPI', __name__)

@blueprintApi.get('/ping')
def getResponse():
    with grpc.insecure_channel('srv_time:50000') as channel:
        stub = retrieve_time_pb2_grpc.RetrieveTimeStub(channel)
        #test de conexion entre servicios
        retrieve = retrieve_time_pb2.EmptyMessage()
        result = stub.PingRetrieveTime(retrieve)

        return {'ack':result.ack}

@blueprintApi.get('/epochtime')
def getTime():
    with grpc.insecure_channel('srv_time:50000') as channel:
        stub = retrieve_time_pb2_grpc.RetrieveTimeStub(channel)
        #test de consulta epoch
        retrieve = retrieve_time_pb2.EmptyMessage()
        result = stub.SendRetrieveTime(retrieve)
       
        return {'time':result.time}

@blueprintApi.get('/time')
def getTimezone():
    global request
    zone = request.args.get('timezone')

    with grpc.insecure_channel('srv_time:50000') as channel:
        stub = retrieve_time_pb2_grpc.RetrieveTimeStub(channel)
        retrieve = retrieve_time_pb2.RetrieveTimezoneRequest(timezone=zone)
        result = stub.SendRetrieveTimeTimezone(retrieve)

        data = {
            'timezone':result.timezone,
            'timeData':result.timeData,
            'currentTime':result.currentTime
        }

        return data