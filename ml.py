from tradingSimulator import TradingSimulator
class ML():
    def __init__(self):
        self.stock = "Bitcoin"
        self.strategy = "TDQN"
        self.simulator = TradingSimulator()

    def run(self):
        self.simulator.simulateNewStrategy(self.strategy, self.stock, saveStrategy=False)
        return "Running";