class Linear(Layer):
    def __init__(self, in_dim, out_dim):
        super().__init__()
        self.W = Tensor(np.random.randn(in_dim, out_dim) * 0.02, requires_grad=True)
        self.b = Tensor(np.zeros(out_dim), requires_grad=True)
        self.parameters = [self.W, self.b]
    
    def forward(self, x):
        return x @ self.W + self.b
