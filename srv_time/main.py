import grpc
import retrieve_time_pb2_grpc
from concurrent import futures

from repository import RetrieveTime

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    retrieve_time_pb2_grpc.add_RetrieveTimeServicer_to_server(RetrieveTime(), server)
    server.add_insecure_port('[::]:50000')
    server.start()
    print("server started, port: 50000")
    server.wait_for_termination()

if __name__ == "__main__":
    main()