class Operator:
    def forward(self, ctx, *inputs):
        """前向传播"""
        raise NotImplementedError

    def backward(self, ctx, grad):
        """反向传播"""
        raise NotImplementedError
