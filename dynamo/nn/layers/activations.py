class ReLU:
    @staticmethod
    def forward(x):
        mask = x.data > 0
        return Tensor(mask * x.data)
    
    @staticmethod
    def backward(grad, x):
        mask = x.data > 0
        return grad * mask
