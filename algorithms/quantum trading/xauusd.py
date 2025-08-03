import yfinance as yf
import matplotlib.pyplot as plt

xauusd = yf.download('XAUUSD=X', start='2022-01-01')

plt.figure(figsize=(14, 6))
plt.plot(xauusd['Close'], label='XAUUSD')
plt.title('Precio')
plt.legend()
plt.grid()
plt.show()
