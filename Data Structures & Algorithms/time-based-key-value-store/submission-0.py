from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]

        # Binary search for the rightmost timestamp <= given timestamp
        i = bisect.bisect_right(arr, (timestamp, chr(127)))

        if i == 0:
            return ""

        return arr[i - 1][1]