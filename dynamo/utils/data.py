class DataLoader:
    def __init__(self, dataset, batch_size=32, shuffle=True):
        self.dataset = dataset
        self.batch_size = batch_size
    
    def __iter__(self):
        indices = np.arange(len(self.dataset))
        for i in range(0, len(indices), self.batch_size):
            yield self.dataset[indices[i:i+self.batch_size]]
