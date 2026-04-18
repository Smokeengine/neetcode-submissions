class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)        
        self.group = defaultdict(list)       
        self.maxfreq = 0

    def push(self, val: int) -> None:
        self.count[val] += 1
        freq = self.count[val]
        self.maxfreq = max(self.maxfreq, freq)
        self.group[freq].append(val)

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()  
        self.count[val] -= 1
        if not self.group[self.maxfreq]:      
            self.maxfreq -= 1
        return val