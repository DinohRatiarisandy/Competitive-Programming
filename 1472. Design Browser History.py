from collections import deque as dq

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page = 0

    def visit(self, url: str) -> None:
        self.history.insert(self.current_page+1, url)
        self.history = self.history[:self.current_page+2]
        self.current_page = len(self.history)-1


    def back(self, steps: int) -> str:
        backward = self.history[:self.current_page+1].copy()

        if steps>=len(backward):
            self.current_page = 0
            return self.history[0]

        while backward:
            backward.pop()
            steps -= 1
            if steps==0:
                try:
                    self.current_page = len(backward)-1
                    return backward[-1]
                except IndexError:
                    return self.history[0]


    def forward(self, steps: int) -> str:
        s = steps
        forward = dq(self.history[self.current_page:].copy())
    
        if steps>=len(forward):
            self.current_page = len(self.history)-1
            return self.history[-1]

        while forward:
            forward.popleft()
            steps -= 1
            if steps==0:
                try:
                    self.current_page += s
                    return forward[0]
                except IndexError:
                    return self.history[len(self.history)-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)