import sys
sys.path.append('.')
from models.CoinbasePro import CoinbasePro
import matplotlib.pyplot as plt

class TradingGraphs():
    def __init__(self, coinbasepro):
        if not isinstance(coinbasepro, CoinbasePro):
            raise TypeError('Coinbase Pro model required.')

        self.coinbasepro = coinbasepro
        self.df = coinbasepro.getDataFrame()
        self.levels = coinbasepro.getSupportResistanceLevels()

    def renderPriceEMA12EMA26(self):
        ''' Render Price, EMA12 and EMA26 '''

        plt.subplot(111)
        plt.plot(self.df.close, label="price")
        plt.plot(self.df.ema12, label="ema12")
        plt.plot(self.df.ema26, label="ema26")
        plt.legend()
        plt.ylabel('Price')
        plt.show()

    def renderPriceSupportResistance(self):
        ''' Render Price, Support and Resistance Levels '''

        plt.subplot(111)
        plt.plot(self.df.close)
        plt.legend()
        plt.ylabel('Price')
        plt.xlabel('Days')

        for level in self.levels:
            plt.hlines(level[1], xmin=level[0], xmax=len(self.df), colors='blue')
       
        plt.show()

    def renderEMAandMACD(self):
        ''' Render Price, EMA12, EMA26 and MACD '''

        ax1 = plt.subplot(211)
        plt.plot(self.df.close, label="price")
        plt.plot(self.df.ema12, label="ema12")
        plt.plot(self.df.ema26, label="ema26")
        plt.legend()
        plt.ylabel('Price')
        plt.subplot(212, sharex=ax1)
        plt.plot(self.df.macd, label="macd")
        plt.plot(self.df.signal, label="signal")
        plt.legend()
        plt.ylabel('Price')
        plt.xlabel('Days')
        plt.show()

    def renderSMAandMACD(self):
        ''' Render Price, SMA20, SMA50, and SMA200 '''

        ax1 = plt.subplot(211)
        plt.plot(self.df.close, label="price")
        plt.plot(self.df.sma20, label="sma20")
        plt.plot(self.df.sma50, label="sma50")
        plt.plot(self.df.sma200, label="sma200")
        plt.legend()
        plt.ylabel('Price')
        plt.subplot(212, sharex=ax1)
        plt.plot(self.df.macd, label="macd")
        plt.plot(self.df.signal, label="signal")
        plt.legend()
        plt.ylabel('Price')
        plt.xlabel('Days')
        plt.show()
