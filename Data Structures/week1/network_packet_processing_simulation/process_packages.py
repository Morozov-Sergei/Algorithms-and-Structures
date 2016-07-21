# python3
import os

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        while self.finish_time_:
            if self.finish_time_[0] <= request.arrival_time:
                self.finish_time_.pop(0)
            else:
                break

        if not len(self.finish_time_):
            self.finish_time_.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        else:
            if len(self.finish_time_) < self.size:
                self.finish_time_.append((request.arrival_time if request.arrival_time > self.finish_time_[-1] else self.finish_time_[-1] )
                    + request.process_time)
                return Response(False, request.arrival_time if request.arrival_time > self.finish_time_[-2] else self.finish_time_[-2] )
            else:
                return Response(True, -1)

def ReadRequests(count):
    requests = []
    for _ in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ReadRequestsFromFile(count, file):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, file.readline().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":

    def prod():
        size, count = map(int, input().strip().split())
        requests = ReadRequests(count)

        buffer = Buffer(size)
        responses = ProcessRequests(requests, buffer)

        PrintResponses(responses)

    def test():
        test_input = [name for name in os.listdir('./tests') if 'a' not in name]
        test_output = [name for name in os.listdir('./tests') if 'a' in name]
        index = 1
        for input_val, output_val in list(zip(test_input,test_output)):
            with open('./tests/' + input_val) as src, open('./tests/' + output_val) as res:
                index += 1
                size, count = map(int, src.readline().strip().split())
                requests = ReadRequestsFromFile(count, src)
                buffer = Buffer(size)
                responses = ProcessRequests(requests, buffer)
                #print('result')
                #PrintResponses(responses)
                for response in responses:
                     assert((response.start_time if not response.dropped else -1) == int(res.readline()))

    prod()
