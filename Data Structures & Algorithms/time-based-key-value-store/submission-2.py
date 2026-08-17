class TimeMap:

    def __init__(self):
        self.key_to_values = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_to_values:
            self.key_to_values[key] = []
        
        self.key_to_values[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_values:
            return ""

        timestamps_values = self.key_to_values[key]
        L, R = 0, len(timestamps_values)-1

        res = [-1, ""]
        while L<=R:
            M = (L+R)//2

            if timestamps_values[M][0] < timestamp:
                if timestamps_values[M][0] > res[0]:
                    res = [timestamps_values[M][0], timestamps_values[M][1]]
                L = M + 1
            elif timestamps_values[M][0] > timestamp:
                R = M - 1
            else:
                return timestamps_values[M][1]

        return res[1]


        
            
        
