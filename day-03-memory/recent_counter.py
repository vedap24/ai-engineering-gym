from collections import deque

class RecentCounter:
    def __init__(self):
        # Meeru cheppina super-fast deque idi
        self.queue = deque()

    def ping(self, t: int) -> int:
        # 1. Kotha ping time ni queue loki add chesthunnam
        self.queue.append(t)
        
        # 2. Patha pings (3000ms kante mundu vi) remove chesthunnam
        # Condition: Queue lo evaraina undali AND first person time pathadi ayi undali
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft() # Meeru cheppina fast remove method!
            
        # 3. Ippudu line lo entha mandi unnaro count return chesthunnam
        return len(self.queue)

# Testing the code
counter = RecentCounter()
print(counter.ping(1))    # Returns 1 (Queue: [1])
print(counter.ping(100))  # Returns 2 (Queue: [1, 100])
print(counter.ping(3001)) # Returns 3 (Queue: [1, 100, 3001])
print(counter.ping(3002)) # Returns 3 (Queue: [100, 3001, 3002] -> '1' was popped!)