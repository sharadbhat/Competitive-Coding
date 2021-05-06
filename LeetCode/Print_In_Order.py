# Leetcode
# https://leetcode.com/problems/print-in-order/

from threading import Lock


class Foo:
    def __init__(self):
        self.first_done = Lock()
        self.second_done = Lock()
        self.first_done.acquire()
        self.second_done.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.first_done:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.second_done.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.second_done:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
