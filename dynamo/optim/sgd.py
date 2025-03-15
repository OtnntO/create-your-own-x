class SGD(Optimizer):
    def step(self):
        for p in self.params:
            if p.grad is None: continue
            p.data -= self.lr * p.grad
