class TimeMap:

    def __init__(self):
        self.key_to_val = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_to_val:
            self.key_to_val[key] = []

        self.key_to_val[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_to_val:
            return ""

        values = self.key_to_val[key]

        res = ""
        L, R = 0, len(values)-1
        while L<=R:
            M = (L+R)//2

            if values[M][0] < timestamp:
                res = values[M][1]
                L = M + 1
            elif values[M][0] > timestamp:
                R = M - 1
            else:
                return values[M][1]

        return res
            
        
