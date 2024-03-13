import grpc
import time
import clock_pb2
import clock_pb2_grpc

def get_local_time():
    return int(time.time() * 1000)

def synchronize_clock(stub):
    local_time = get_local_time()
    response = stub.GetTime(clock_pb2.TimeRequest())
    server_time = response.timestamp

    print("Tempo do cliente:", local_time)
    print("Tempo do servidor:", server_time)

    adjustment = stub.SyncTime(clock_pb2.SyncRequest(slave_times=[clock_pb2.TimeResponse(timestamp=local_time)]))
    print("Ajuste de tempo:", adjustment.adjustment)

    adjusted_time = local_time + adjustment.adjustment
    print("Tempo ajustado:", adjusted_time)

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = clock_pb2_grpc.ClockSynchronizerStub(channel)
        synchronize_clock(stub)

if __name__ == '__main__':
    run()
