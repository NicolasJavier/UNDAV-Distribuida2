import time
from pytz import timezone
from datetime import datetime
import retrieve_time_pb2
import retrieve_time_pb2_grpc


class RetrieveTime(retrieve_time_pb2_grpc.RetrieveTimeServicer):
    def PingRetrieveTime(self, request, context):
        response = retrieve_time_pb2.PingRetrieveTimeResponse(ack='1')
        return response

    def SendRetrieveTime(self, request, context):
        epochTime = time.time()
        response = retrieve_time_pb2.RetrieveTimeResponse(time=epochTime)
        return response

    def SendRetrieveTimeTimezone(self, request, context):
        zone = str(request.timezone)

        requiredTimezone = timezone(zone)
        fmt = '%y/%m/%d %H:%M:%S %Z%z'
        timezoneNow = datetime.now(requiredTimezone)
        formattedTime = str(datetime.strftime(timezoneNow,fmt))
        
        epochTime = time.time()

        data = retrieve_time_pb2.RetrieveTimezoneResponse(timezone=zone, timeData=formattedTime, currentTime=epochTime)
        return data
