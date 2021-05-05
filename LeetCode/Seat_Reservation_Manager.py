# Leetcode
# https://leetcode.com/problems/seat-reservation-manager/

from heapq import heapify, heappush, heappop


class SeatManager:

    def __init__(self, n: int):
        self.free = [i for i in range(1, n + 1)]
        heapify(self.free)

    def reserve(self) -> int:
        return heappop(self.free)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.free, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
