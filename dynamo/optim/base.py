class Optimizer:
    def __init__(self, params, lr=0.01):
        self.params = [p for p in params if p.requires_grad]
        self.lr = lr
    
    def step(self):
        raise NotImplementedError
    
    def zero_grad(self):
        for p in self.params:
            p.grad = None
