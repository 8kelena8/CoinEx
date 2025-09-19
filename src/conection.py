import ccxt
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

# Configurar API de Coinex
coinex = ccxt.coinex({
    'apiKey': 'A1A0693A396F4C6689CA4BE2E3471BF2',
    'secret': '50325007855963F59B2C84ED97DC7B276D86D76432B332EB',
    'enableRateLimit': True,
})

# Verificar conexión
# print(coinex.fetch_balance())

def obtener_datos_historicos(symbol='GRT/USDT', timeframe='1min', limit=1000):
    """
    Obtiene datos históricos de Coinex
    """
    ohlcv = coinex.fetch_ohlcv(symbol, timeframe, limit=limit, since=1758183360000)
    # print(ohlcv)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp_date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    ruta_completa = os.path.join('/home/kelena/workspace/CoinEx/src/data/prueba.csv')
    df.to_csv(ruta_completa, encoding='utf-8')
    return df

# Obtener datos
df = obtener_datos_historicos('GRT/USDT', '1min', 1000)
print(df.head())

