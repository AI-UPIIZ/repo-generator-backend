import pandas as pd

from consts.consts import DatasetSplit, Metadata
from consts.paths import INTER_DATA


def split(dataset, save_file=False):
    train_df = dataset.sample(frac=0.8)
    train_df[Metadata.SUBSET] = DatasetSplit.TRAIN

    test_df = dataset.drop(train_df.index)
    test_df = test_df.sample(frac=0.5)
    test_df[Metadata.SUBSET] = DatasetSplit.TEST

    val_df = dataset.drop(train_df.index)
    val_df = val_df.drop(test_df.index)
    val_df[Metadata.SUBSET] = DatasetSplit.VAL

    df = pd.concat([train_df, test_df, val_df], ignore_index=True)
    
    if save_file:
        df.to_csv(INTER_DATA)

    return df
