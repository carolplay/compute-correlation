# compute-correlation

correlation.ipynb is for exploring the problem and data sources.

compute-correlation.py is the program for computing correlation.
Sample usage:
```bash
python -m compute-correlation --start_date 2017-01-01 --last_date 2017-01-11 --stocks AAPL MSFT GOOG TSLA FB AMZN BABA
```
Unavailable stock data will be automatically downloaded from Yahoo.
