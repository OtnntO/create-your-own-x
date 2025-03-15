# 测试用例示例 (tests/test_autograd.py)
def test_add_backward():
    a = Tensor([2], requires_grad=True)
    b = Tensor([3], requires_grad=True)
    c = a + b
    c.backward()
    assert a.grad == 1 and b.grad == 1
