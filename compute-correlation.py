import pandas as pd
import pandas_datareader as pdr
from datetime import datetime
import os
import argparse


def fetch_stock_price(stock):
    """
    :param stock:
    :return: stock price data frame fetched from provider
    package retry decorator could help reduce issue of yahoo not returning data
    """
    provider = 'yahoo'
    df = pdr.DataReader(stock, provider)
    df.to_csv(os.path.join('data','{}.csv'.format(stock)))
    return df


def get_stock_price(start_date, last_date, stock, col='Close'):
    """
    :param start_date:
    :param last_date:
    :param stock:
    :param col:
    :return: Close price of a stock over a period
    """
    try:
        df = pd.read_csv(os.path.join('data','{}.csv'.format(stock)),
                         header=0, index_col=0, parse_dates=True)
    except FileNotFoundError:
        df = fetch_stock_price(stock)

    return df.loc[start_date:last_date, col]


def compute_correlation(start_date, last_date, stocks):
    """
    :param start_date:
    :param last_date:
    :param stocks:
    :print correlation results
    """
    if stocks and start_date < last_date:
        prices = pd.concat([get_stock_price(
            start_date, last_date, s) for s in stocks],
            axis=1, keys=stocks)

        if len(prices) > 1 and len(prices.columns) > 1:
            cor = prices.corr()
            print(cor)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Compute the correlation between multiple stocks.')
    parse_dt = lambda t: datetime.strptime(t, '%Y-%m-%d')
    parser.add_argument('--start_date', type=parse_dt, required=True,
                        help='format: 2001-01-01')
    parser.add_argument('--last_date', type=parse_dt, required=True)
    parser.add_argument('--stocks', nargs='+')
    args = parser.parse_args()

    compute_correlation(args.start_date, args.last_date, args.stocks)
