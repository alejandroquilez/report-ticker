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
=== REPORTE DE TSLA ===

- - - DATOS DE MERCADO - - -
Precio Actual: $396.73
Cambio 24h: -8.82 (-2.1748%)
Volumen: 64,054,561
Rango del día: $394.21 - $402.35

- - - RESUMEN DE SENTIMENT ===
Total noticias: 10
Positivas: 0 (0.00%)
Neutrales: 7 (70.00%)
Negativas: 3 (30.00%)
Sentimiento General: NEGATIVO
Score Promedio: -0.17

[Chart visualization saved]
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
