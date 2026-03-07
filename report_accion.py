
import requests
import time
from bs4 import BeautifulSoup
import yfinance as yf
from matplotlib import pyplot as plt
from datetime import datetime, date

ticker = input("Introduzca una acción (p.e. NVDA, AAPL, TSLA,...):")
apikey = input("Introduzca su API key de Alpha Vantage:")

def obtener_datos_mercado(ticker, apikey):
    
    COTIZACION = "GLOBAL_QUOTE"
    
    url = "https://www.alphavantage.co/query"
    params1 = {
        "symbol" : ticker,
        "function" : COTIZACION,
        "apikey" : apikey,
    }
    
    r1 = requests.get(url, params = params1 )
    
    print("Obteniendo Cotización...")
    
    if r1.status_code != 200:
        print(f"Error en la petición 1: {r1.status_code}")
        return None
    
    cotizacion_raw = r1.json()
    print("Respuesta Obtenida")
    
    if 'Global Quote' in cotizacion_raw:
        cotizacion = cotizacion_raw['Global Quote']
    else :
        print("No se encontró la cotización en la petición 1.")
        return None
    
    datos = {
        'symbol': cotizacion.get('01. symbol', ticker),
        'price' : float(cotizacion.get('05. price', 0)),
        'change': float(cotizacion.get('09. change', 0)),
        'percent_change': cotizacion.get('10. change percent', '0%'),
        'volume': int(cotizacion.get('06. volume', 0)),
        'open': float(cotizacion.get('02. open', 0)),
        'high': float(cotizacion.get('03. high', 0)),
        'low': float(cotizacion.get('04. low', 0)),
        'previous_close': float(cotizacion.get('08. previous close', 0)),
        'latest_trading_day': cotizacion.get('07. latest trading day', 'N/A')    
             
    }
    return datos

def scrapear_noticias(ticker):
    
    url = f"https://finviz.com/quote.ashx?t={ticker}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    print('Scraping noticias...')
    r = requests.get(url, headers = headers)
    
    if r.status_code != 200:
        print(f"Error al acceder a Finviz: {r.status_code}")
        return []
        
        
    texto_noticias = BeautifulSoup(r.text, 'html.parser')
    tabla = texto_noticias.find('table', { 'id' : 'news-table'})
    
    lista_noticias = tabla.find_all('tr')
    
    if tabla is None:
        print("No se encontraron noticias")
        return []
    
    noticias = []
    
    for fila in lista_noticias:
        
        celdas = fila.find_all('td')
        
        if len(celdas)<2: 
            continue
        
        fecha = celdas[0].text

        
        link = fila.find('a')
        if link: 
            titulo = link.text.strip()
        else:
            titulo = 'Sin título'
            
        span = fila.find('span') 
        if span: 
            fuente = span.text.strip()
        else: 
            fuente = 'Desconocido'
        
        
        noticia = {
            'fecha': fecha,
            'titulo': titulo,
            'fuente': fuente   
        }
        
        noticias.append(noticia)
    
    
    return noticias

def analizar_sentiment(texto):
    
    alcistas = ['up', 'gain', 'rise', 'surge', 'profit', 'beat', 'strong', 
    'growth', 'bullish', 'rally', 'soar', 'high', 'record', 
    'boost', 'jump', 'outperform', 'upgrade', 'buy']
    
    bajistas = ['down', 'fall', 'drop', 'loss', 'weak', 'decline', 'bearish',
    'crash', 'plunge', 'miss', 'cut', 'low', 'sell', 'downgrade',
    'concern', 'risk', 'slump', 'tumble']
    
    # Podría particularizar más con palabras muy negativas o muy positivas, 
    # o dandole más peso si se menciona el ticker, por ejemplo
        
    pos_count = 0
    neg_count = 0
               
    for palabra in alcistas:
        if palabra in texto.lower():
            pos_count += 1
                
    for palabra in bajistas:
        if palabra in texto.lower():
            neg_count += 1
                
    score = (pos_count - neg_count) / (pos_count + neg_count + 1)

    if score < -0.2:
        sentiment = 'Negativo'
    elif score > 0.2:
        sentiment = 'Positivo'
    else:
        sentiment = 'Neutro'

    return  {
        'sentiment': sentiment,
        'score' : score
    }


def generar_reporte(ticker, datos_mercado, noticias):
    
    print(f"=== REPORTE DE {ticker.upper()} ===\n")
    
    
    print("- - - DATOS DE MERCADO - - -")
    print(f"Precio Actual: ${datos_mercado['price']}")
    print(f"Cambio 24h: {datos_mercado['change']:+.2f} ({datos_mercado['percent_change']})")
    print(f"Volumen: {datos_mercado['volume']:,}")
    print(f"Rango del día: ${datos_mercado['low']:.2f} - ${datos_mercado['high']:.2f}")
    print(f"Último día de trading: {datos_mercado['latest_trading_day']}")
    print(f"\n")
    
  
    for noticia in noticias:
        rdo = analizar_sentiment(noticia['titulo'])
    
        noticia['sentiment'] = rdo['sentiment']
        noticia['score'] = rdo['score']
    

    
    print(f"- - - NOTICIAS RECIENTES (10) - - -") 
    positivo = 0
    neutro = 0
    negativo = 0
    score_total = 0
    
    for i, noticia in enumerate(noticias[:10], 1):
        estado = 'Bullish' if noticia['sentiment'] == 'Positivo' else 'Bearish' if noticia['sentiment'] == 'Negativo' else 'Neutro'
        print(f"\n{i}. [{noticia['fecha']}] {estado} ({noticia['score']:.2f})")
        print(f"Título: {noticia['titulo']}")
        print(f"Fuente: {noticia['fuente']} \n")
        
        score_total += noticia['score']
        
        if estado == 'Bullish':
            positivo += 1
        elif estado == 'Bearish':
            negativo += 1
        else:
            neutro += 1
    
    prop_pos = (positivo/(10))  * 100  
    prop_neg = (negativo/(10))  * 100 
    prop_neu = (neutro/(10))  * 100 
    score_promedio = score_total / 10
    
    if score_promedio > 0.1 : 
        sentimiento_general = 'Positivo'
    elif score_promedio < -0.1 :
        sentimiento_general = 'Negativo'
    else:
        sentimiento_general = 'Neutro'
        
    print("=== RESUMEN DE SENTIMENT ===\n")
    print(f"Total noticias analizadas: 10")
    print(f"Positivas: {positivo} ({prop_pos:.2f}%)")
    print(f"Neutrales: {neutro} ({prop_neu:.2f}%)")
    print(f"Negativas: {negativo} ({prop_neg:.2f}%)")
    print(f"Sentimiento General: {sentimiento_general.upper()}")
    print(f"Score Promedio: {score_promedio:+.2f}")
    
def visualizar_ticker(ticker, noticias):
    
    datos_mensuales = yf.Ticker(ticker).history(period = '1mo')

    if datos_mensuales.empty:
        print('No se encontraron datos históricos.')
        return 
    
    fig, ax = plt.subplots(figsize = (14, 7))
    
    ax.plot(datos_mensuales.index, datos_mensuales['Close'], linewidth = 2, color = 'b', label = 'Precio')
    
    for noticia in noticias:
        
        fecha_noticia = noticia['fecha'].strip()
        
        try:
            if "-" in fecha_noticia:
                fecha_obj = datetime.strptime(fecha_noticia, '%b-%d-%y %I:%M%p')
            else:
                fecha_obj = datetime.now()
            
            fecha_date = fecha_obj.date()
            

            for timestamp in datos_mensuales.index:
                if timestamp.date() == fecha_date:
                    precio = datos_mensuales.loc[timestamp, 'Close']
                    
                    sentiment = noticia['sentiment']
                    
                    if sentiment == 'Positivo':
                        color = 'green'
                        marker = '^'
                    elif sentiment == 'Negativo':
                        color = 'red'
                        marker = 'v'
                    else:
                        color = 'grey'
                        marker = 'o'
                        
                    
                    ax.scatter(timestamp, precio, color = color, marker = marker, s=200, zorder=5, edgecolors='black', linewidths=1)
                    break
                
        except Exception as e:
            
            print(f"No se pudo parsear la fecha: {fecha_noticia} - {e}")
            continue
        
    ax.set_title(f"Timeline de noticias: {ticker}", fontsize = 16, fontweight = 'bold') 
    ax.set_ylabel("Precio ($)", fontsize = 12)
    ax.set_xlabel("Fecha", fontsize = 12)
    
    ax.scatter([], [], marker='^', color='green', s=200, 
               label='Noticia Positiva', edgecolors='black')
    ax.scatter([], [], marker='v', color='red', s=200, 
               label='Noticia Negativa', edgecolors='black')
    ax.scatter([], [], marker='o', color='gray', s=100, 
               label='Noticia Neutral', edgecolors='black')
    ax.legend(loc='best')

    plt.grid(True, alpha = 0.3)
    plt.xticks(rotation = 45)
    plt.tight_layout()
    
    filename = f"Timeline_{ticker}.jpg"
    plt.savefig(filename, dpi = 300, bbox_inches = 'tight')
    print(f"\n Gráfico de {ticker} guardado.")
    
    plt.show()
    
    

datos_mercado = obtener_datos_mercado(ticker, apikey)

noticias = scrapear_noticias(ticker)

if  datos_mercado and noticias:
    generar_reporte(ticker, datos_mercado, noticias)
else:
    print("No hay suficientes datos para hacer un reporte.")
    
visualizar_ticker(ticker, noticias)

    
