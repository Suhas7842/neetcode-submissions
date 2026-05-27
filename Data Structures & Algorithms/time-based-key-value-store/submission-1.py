class TimeMap:

    def __init__(self):
        self.stats = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stats[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        time_values = self.stats[key]
        l, r = 0, len(time_values) - 1
        while l<= r : 
            m = l + (r -l )//2
            if time_values[m][1] <= timestamp : 
                l = m + 1
            elif time_values[m][1] > timestamp:
                r = m - 1
            else :
                return time_values[m][0]
        return time_values[r][0] if r>=0 else ""