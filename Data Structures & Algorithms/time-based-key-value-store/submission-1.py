class TimeMap:

    def __init__(self):
        self.ms = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.ms:
            self.ms[key] = []
        self.ms[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        v = self.ms.get(key, []) # will return value, timestamp
        l = 0
        r = len(v) - 1
        res = ""
        
        while l <= r:
            mid = l + (r-l)//2

            if v[mid][1] == timestamp:
                res = v[mid][0]
                break
            elif v[mid][1] < timestamp:
                res = v[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res


            
'''
alice:  happy, 1 | happy, 2
bob:    sad, 3   | sad, 4
'''

        