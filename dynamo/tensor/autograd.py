class AutogradEngine:
    def backward(self, tensor, grad=None):
        # 拓扑排序计算图
        sorted_nodes = topological_sort(tensor)
        tensor.grad = grad if grad else np.ones_like(tensor.data)
        
        # 逆序传播梯度
        for node in reversed(sorted_nodes):
            node._backward()
