import yfinance as yf
import matplotlib.pyplot as plt

xauusd = yf.download('XAUUSD=X', start='2022-01-01')
usdx = yf.download('DX-Y.NYB', start='2022-01-01')  # USD Index

plt.figure(figsize=(14, 6))
plt.plot(xauusd['Close'], label='XAUUSD')
plt.plot(usdx['Close'], label='USDX')
plt.title('Comparativa: XAUUSD vs USDX')
plt.legend()
plt.grid()
plt.show()