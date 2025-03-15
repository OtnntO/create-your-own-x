class TransposeOp(Operator):
    def forward(self, ctx, x):
        return x.data.T

    def backward(self, ctx, grad):
        return grad.T

def transpose(self):
    op = TransposeOp()
    result_data = op.forward(None, self)
    result = Tensor(result_data, requires_grad=self.requires_grad)
    result._op = op
    result._ctx = [self]
    return result

Tensor.T = property(transpose)
