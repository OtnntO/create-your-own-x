# 加法运算符示例 (tensor/ops/math_ops.py)
class AddOp:
    @staticmethod
    def forward(ctx, a, b):
        ctx.save_for_backward(a, b)
        return Tensor(a.data + b.data)
    
    @staticmethod
    def backward(ctx, grad):
        a, b = ctx.saved_tensors
        return grad, grad  # 加法梯度传播规则# 加法运算符示例 (tensor/ops/math_ops.py)
class AddOp:
    @staticmethod
    def forward(ctx, a, b):
        ctx.save_for_backward(a, b)
        return Tensor(a.data + b.data)
    
    @staticmethod
    def backward(ctx, grad):
        a, b = ctx.saved_tensors
        return grad, grad  # 加法梯度传播规则
