from urllib import request
import grpc
import retrieve_time_pb2
import retrieve_time_pb2_grpc

def main():
    with grpc.insecure_channel('srv_time:50000') as channel:
        stub = retrieve_time_pb2_grpc.RetrieveTimeStub(channel)
        request = retrieve_time_pb2.EmptyMessage()
        result = stub.PingRetrieveTime(request)
        print(f'GRPC recived: {result.ack}')

if __name__ == "__main__":
    main()