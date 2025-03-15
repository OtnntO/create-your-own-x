import numpy as np

class Tensor:
    def __init__(self, data, requires_grad=False, dtype=None):
        # 支持从 numpy 数组自动转换
        if not isinstance(data, np.ndarray):
            data = np.array(data, dtype=dtype)
        
        self.data = data                # 存储张量数据（numpy 数组）
        self.grad = None                # 梯度存储
        self.requires_grad = requires_grad  # 是否追踪梯度
        self._op = None                 # 记录创建该张量的运算符（用于计算图）
        self._ctx = []                   # 上下文（父节点张量）

        # 统一数据类型（如 float32）
        if dtype is not None:
            self.data = self.data.astype(dtype)

    @property
    def shape(self):
        return self.data.shape
    
    @property
    def dtype(self):
        return self.data.dtype

    def zero_grad(self):
        """清除梯度"""
        self.grad = np.zeros_like(self.data)

    def backward(self, grad=None):
        """反向传播入口"""
        if grad is None:
            grad = np.ones_like(self.data)
        self.grad = grad
        
        # 递归反向传播（需实现运算符的 backward 方法）
        if self._op is not None:
            self._op.backward(self._ctx, grad)

    def __repr__(self):
        return f"Tensor({self.data}, requires_grad={self.requires_grad})"

    # 以下为与 NumPy 互操作的方法
    @classmethod
    def from_numpy(cls, array, requires_grad=False):
        """从 numpy 数组创建 Tensor"""
        return cls(array, requires_grad=requires_grad)

    def numpy(self):
        """转换为 numpy 数组（不保留计算图）"""
        return self.data.copy()
