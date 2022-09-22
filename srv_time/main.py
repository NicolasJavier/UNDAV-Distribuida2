import grpc
import retrieve_time_pb2
import retrieve_time_pb2_grpc
from concurrent import futures

class RetrieveTime(retrieve_time_pb2_grpc.RetrieveTimeServicer):
    def PingRetrieveTime(self, request, context):
        response = retrieve_time_pb2.PingRetrieveTimeResponse(ack='1')
        return response

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    retrieve_time_pb2_grpc.add_RetrieveTimeServicer_to_server(RetrieveTime(), server)

    #server.add_secure_port('[::]:50000')
    server.add_insecure_port('[::]:50000')
    server.start()
    print("server started, port: 50000")
    server.wait_for_termination()

if __name__ == "__main__":
    main()