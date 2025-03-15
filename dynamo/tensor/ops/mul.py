class MulOp(Operator):
    def forward(self, ctx, a, b):
        ctx.save_for_backward(a, b)
        return a.data * b.data

    def backward(self, ctx, grad):
        a, b = ctx.saved_tensors
        if a.requires_grad:
            a.grad += grad * b.data
        if b.requires_grad:
            b.grad += grad * a.data

def _mul_(self, other):
    other = other if isinstance(other, Tensor) else Tensor(other)
    op = MulOp()
    ctx = [self, other]
    result_data = op.forward(ctx, self, other)
    result = Tensor(result_data, requires_grad=(self.requires_grad or other.requires_grad))
    result._op = op
    result._ctx = ctx
    return result

Tensor.__mul__ = _mul_
