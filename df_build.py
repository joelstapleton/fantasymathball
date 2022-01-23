import pandas as pd


def source():
    return pd.read_csv('https://github.com/guga31bb/nflfastR-data/blob/master/data/play_by_play_2021.csv.gz?raw=True',
                       compression='gzip', low_memory=False)
