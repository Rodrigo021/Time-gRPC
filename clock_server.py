from concurrent import futures
import time
import grpc
import clock_pb2
import clock_pb2_grpc
import statistics

class ClockServer(clock_pb2_grpc.ClockSynchronizerServicer):
    def GetTime(self, request, context):
        return clock_pb2.TimeResponse(timestamp=int(time.time() * 1000))

    def SyncTime(self, request, context):
        slave_times = request.slave_times
        slave_timestamps = [slave.timestamp for slave in slave_times]
        avg_slave_time = statistics.mean(slave_timestamps)

        master_time = int(time.time() * 1000)
        adjustment = avg_slave_time - master_time

        return clock_pb2.SyncResponse(adjustment=adjustment)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    clock_pb2_grpc.add_ClockSynchronizerServicer_to_server(ClockServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
