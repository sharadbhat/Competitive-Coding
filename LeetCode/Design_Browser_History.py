# Leetcode
# https://leetcode.com/problems/design-browser-history/


class BrowserHistory:

    def __init__(self, homepage: str):
        self.backwardStack = []
        self.forwardStack = []
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.backwardStack.append(self.curr)
        self.forwardStack = []
        self.curr = url

    def back(self, steps: int) -> str:
        if not len(self.backwardStack):
            return self.curr

        for i in range(min(steps, len(self.backwardStack))):
            self.forwardStack.append(self.curr)
            self.curr = self.backwardStack.pop()

        return self.curr

    def forward(self, steps: int) -> str:
        if not len(self.forwardStack):
            return self.curr

        for i in range(min(steps, len(self.forwardStack))):
            self.backwardStack.append(self.curr)
            self.curr = self.forwardStack.pop()

        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
