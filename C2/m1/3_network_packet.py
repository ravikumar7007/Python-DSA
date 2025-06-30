from collections import deque

class NetworkBuffer:
    def __init__(self,size: int):
        self.size = size
        self.finish_time = deque()

    def process(self,packets):
        result = []
        for arrival,duration in packets:
            while self.finish_time and self.finish_time[0] <= arrival:
                self.finish_time.popleft()
            if len(self.finish_time) == self.size:
                result.append(-1)
            else:
                start_time = arrival if not self.finish_time else max(arrival, self.finish_time[-1])
                result.append(start_time )
                self.finish_time.append(start_time + duration)
        return result
    
if __name__ == "__main__":
    n, m = map(int, input().split())
    packets = [tuple(map(int, input().split())) for _ in range(m)]
    buffer = NetworkBuffer(n)
    result = buffer.process(packets)
    for res in result:
        print(res)