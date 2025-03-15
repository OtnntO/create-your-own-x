class AddOp(Operator):
    def forward(self, ctx, a, b):
        # 前向传播：记录输入张量到上下文
        ctx.save_for_backward(a, b)
        return a.data + b.data

    def backward(self, ctx, grad):
        # 反向传播：梯度分配给两个输入（加法梯度为1）
        a, b = ctx.saved_tensors
        if a.requires_grad:
            a.grad += grad
        if b.requires_grad:
            b.grad += grad

# 重载 Tensor 的 __add__ 运算符
def _add_(self, other):
    other = other if isinstance(other, Tensor) else Tensor(other)
    op = AddOp()
    ctx = [self, other]
    result_data = op.forward(ctx, self, other)
    result = Tensor(result_data, requires_grad=(self.requires_grad or other.requires_grad))
    result._op = op
    result._ctx = ctx
    return result

Tensor.__add__ = _add_
