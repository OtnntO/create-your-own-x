class Layer:
    def __init__(self):
        self.parameters = []
    
    def forward(self, x):
        raise NotImplementedError
    
    def __call__(self, x):
        return self.forward(x)
