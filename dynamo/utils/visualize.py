class TrainingMonitor:
    def __init__(self):
        self.losses = []
    
    def update(self, loss):
        self.losses.append(loss)
        plt.plot(self.losses)
        plt.draw()
        plt.pause(0.001)
