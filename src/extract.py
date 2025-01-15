import yfinance

def extract_hist_ticker(ticker, start_date, end_date):
    caminho = f'/home/arthur/celery_airflow/{ticker}.csv'
    yfinance.Ticker(ticker).history(
        period= '1d',
        interval= '1h',
        start = start_date,
        end = end_date,
        prepost = True
    ).to_csv(caminho)
    

if __name__ == '__main__':
    hist = extract_hist_ticker('AAPL', '2025-01-14', '2025-01-15')
    hist = extract_hist_ticker('GOOG', '2025-01-14', '2025-01-15')
