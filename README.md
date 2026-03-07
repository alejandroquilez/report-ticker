# Report Completo de un Ticker

Programa de Python que realiza un informe detallado de un ticker, elaborando una lista de datos clave, noticias, analizando el sentimiento del mercado y mostrando un gráfico del comportamiento del mismo en el último mes.

## Funcionalidades

- Uso de APIs para extraer métricas clave
- Webscraping para extraer noticias relevantes
- Informe con los datos del ticker
- Lista de noticias más recientes (10)
- Resumen de sentimiento de mercado

## Tecnologías

- Python 3.14
- requests - webscraping
- BeautifulSoup4 (bs4) - tratamiento de HTML
- yfinance - Descarga de datos financieros
- matplotlib - Visualización de datos

## Instalación
```bash
pip install yfinance requests bs4 matplotlib
```

## Uso
```bash
python report_accion.py
```
El programa pedirá un ticker y una API Key de Alpha Vantage (https://www.alphavantage.co/).

## Ejemplo de salida
```
Obteniendo Cotización...
Respuesta Obtenida
Scraping noticias...
=== REPORTE DE TSLA ===

- - - DATOS DE MERCADO - - -
Precio Actual: $396.73
Cambio 24h: -8.82 (-2.1748%)
Volumen: 64,054,561
Rango del día: $394.21 - $402.35
Último día de trading: 2026-03-06


- - - NOTICIAS RECIENTES (10) - - -

1. [
            Mar-06-26 07:00PM
        ] Neutro (0.00)
Título: The $200 Billion Question: Is Amazon Finally Ready to Pay a Dividend?
Fuente: (Barchart)


2. [
            05:45PM
        ] Neutro (0.00)
Título: Tesla (TSLA) Sees a More Significant Dip Than Broader Market: Some Facts to Know
Fuente: (Zacks)


3. [
            04:42PM
        ] Bearish (-0.67)
Título: Stocks Retreat on Inflation Concerns and a Weak US Job Market
Fuente: (Barchart)


4. [
            04:30PM
        ] Neutro (0.00)
Título: These Stocks Are Todays Movers: Marvell, Gap, Trade Desk, United Airlines, Corning, BlackRock, Tesla, Presidio, and More
Fuente: (Barrons.com)


5. [
            04:22PM
        ] Neutro (0.00)
Título: Tesla Stock Slips. Its Losing Streak Continues.
Fuente: (Barrons.com)


6. [
            10:36AM
        ] Neutro (0.00)
Título: BYD Can Charge an EV in 5 Minutes. What That Means for Tesla.
Fuente: (Barrons.com)


7. [
            04:09PM
        ] Bearish (-0.50)
Título: Oil prices are surging. Will that help Tesla and others sell more EVs?
Fuente: (MarketWatch)


8. [
            03:31PM
        ] Neutro (0.00)
Título: BYD Needs Just 9 Minutes To Challenge Tesla's Last Great Advantage
Fuente: (Benzinga)


9. [
            02:58PM
        ] Bearish (-0.50)
Título: Big Tech stocks slump, weighing on S&P 500
Fuente: (MarketWatch)


10. [
            02:35PM
        ] Neutro (0.00)
Título: Elon Musk Has One Word As Saudi Arabia Eyes Turning $500B Sci-Fi City Into AI Hub
Fuente: (Benzinga)

=== RESUMEN DE SENTIMENT ===

Total noticias analizadas: 10
Positivas: 0 (0.00%)
Neutrales: 7 (70.00%)
Negativas: 3 (30.00%)
Sentimiento General: NEGATIVO
Score Promedio: -0.17

Gráfico de TSLA guardado.

[Timeline_TSLA.jpg]
```

## Aprendizajes

- Mejora en la definición de funciones y el uso de bucles prolongados
- Trabajo nuevas librerías y APIs
- Webscraping y data parsing
- Tratamiento de texto y fechas

## Posibles Mejoras

- Superposicion de noticias en gráfico
- Ampliación del periodo de análisis