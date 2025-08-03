from fredapi import Fred
fred = Fred(api_key='TU_API_KEY_FRED')

tasas = fred.get_series('FEDFUNDS')
desempleo = fred.get_series('UNRATE')

tasas.plot(title='Tasa de Interés Federal')
desempleo.plot(title='Tasa de Desempleo en EE. UU.')
