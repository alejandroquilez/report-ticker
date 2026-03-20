# Ticker Report Generator

## Overview
Generates comprehensive financial reports for stock tickers by integrating real-time market data, sentiment analysis, and technical visualization. Automates the collection and synthesis of market-critical information (pricing, news, sentiment) into actionable intelligence.

## Key Features
- **Real-time market data extraction** via yfinance and Alpha Vantage API
- **Automated news aggregation** with web scraping (BeautifulSoup4)
- **Sentiment analysis** of recent financial news (10 most recent articles)
- **Market sentiment scoring** (bullish/neutral/bearish classification)
- **Technical visualization** - 1-month price chart with volume data
- **Comprehensive reporting** - consolidated ticker analysis in single output

## How It Works
1. Fetches current ticker price, 24h change, volume, day range
2. Scrapes 10 most recent news articles from financial sources
3. Classifies sentiment for each article (bullish/neutral/bearish)
4. Aggregates sentiment data (% positive/neutral/negative, average score)
5. Generates time-series price chart visualization
6. Outputs consolidated report with all metrics

## Tech Stack
- **Python 3.x** - Core language
- **yfinance** - Historical price and volume data
- **Alpha Vantage API** - Real-time market data and sentiment scores
- **requests** - HTTP client for API calls
- **BeautifulSoup4 (bs4)** - HTML parsing for news extraction
- **Matplotlib** - Chart rendering and visualization

## Installation
```bash
pip install yfinance requests beautifulsoup4 matplotlib
```

## Usage
```bash
python report_accion.py
```

**Input:**
- Ticker symbol (e.g., TSLA, AAPL, GOOGL)
- Alpha Vantage API key (free tier available at https://www.alphavantage.co/)

**Output:**
- Console report with market metrics, sentiment breakdown, and news summary
- Chart file (Timeline_[TICKER].jpg) saved to working directory

### Example Output
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


## Skills Demonstrated
- **Data Integration** - Multiple API sources (yfinance, Alpha Vantage)
- **Web Scraping** - Financial news extraction and parsing
- **Sentiment Analysis** - Classification of market sentiment from text
- **Data Visualization** - Time-series charting with Matplotlib
- **Financial Metrics** - Understanding of stock market data structures
- **API Handling** - Authentication, request/response management

## Possible Improvements
- Real-time news feed integration instead of static scraping
- Multi-ticker portfolio analysis in single report
- Extended analysis period (currently 1 month)
- Correlation analysis between sentiment and price movement
- Export to PDF or email delivery

## Author
Alejandro Quílez
