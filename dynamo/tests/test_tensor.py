import numpy as np
import pytest

def test_tensor_creation():
    # 测试从 numpy 转换
    a = Tensor(np.array([1, 2, 3]))
    assert isinstance(a.data, np.ndarray)
    assert a.shape == (3,)

def test_add_operation():
    a = Tensor([1, 2], requires_grad=True)
    b = Tensor([3, 4], requires_grad=True)
    c = a + b
    c.backward()
    assert np.allclose(a.grad, [1, 1])  # 加法梯度应为1

def test_gradient_check():
    # 数值梯度校验
    x = Tensor([2.0], requires_grad=True)
    y = x * 3
    y.backward()
    
    # 数值梯度计算（中心差分）
    eps = 1e-5
    x_plus = Tensor([2.0 + eps], requires_grad=True)
    y_plus = x_plus * 3
    x_minus = Tensor([2.0 - eps], requires_grad=True)
    y_minus = x_minus * 3
    num_grad = (y_plus.data - y_minus.data) / (2 * eps)
    
    assert np.isclose(x.grad, num_grad, rtol=1e-4)
