from concurrent import futures
import time
import grpc
import clock_pb2
import clock_pb2_grpc
import statistics
import threading

class ClockServer(clock_pb2_grpc.ClockSynchronizerServicer):
    def __init__(self):
        self.slave_stubs = []
        self.lock = threading.Lock()

    def GetTime(self, request, context):
        return clock_pb2.TimeResponse(timestamp=int(time.time() * 1000))

    def SyncTime(self, request, context):
        with self.lock:
            slave_times = request.slave_times
            slave_timestamps = [slave.timestamp for slave in slave_times]
            avg_slave_time = statistics.mean(slave_timestamps)

            master_time = int(time.time() * 1000)
            adjustment = avg_slave_time - master_time

            return clock_pb2.SyncResponse(adjustment=adjustment)

    def register_slave_stub(self, stub):
        with self.lock:
            self.slave_stubs.append(stub)

    def adjust_time_for_all_slaves(self):
        with self.lock:
            for stub in self.slave_stubs:
                local_time = int(time.time() * 1000)
                response = stub.GetTime(clock_pb2.TimeRequest())
                server_time = response.timestamp

                adjustment = self.SyncTime(clock_pb2.SyncRequest(slave_times=[clock_pb2.TimeResponse(timestamp=local_time)]))
                adjusted_time = local_time + adjustment.adjustment

                print("Ajustando tempo para cliente:", adjusted_time)
                try:
                    stub.AdjustTime(clock_pb2.AdjustRequest(adjusted_time=adjusted_time))
                except grpc.RpcError as e:
                    print(f"Erro ao ajustar tempo para cliente: {e}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    clock_pb2_grpc.add_ClockSynchronizerServicer_to_server(ClockServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()

    clock_server = ClockServer()
    try:
        while True:
            time.sleep(5)
            clock_server.adjust_time_for_all_slaves()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
