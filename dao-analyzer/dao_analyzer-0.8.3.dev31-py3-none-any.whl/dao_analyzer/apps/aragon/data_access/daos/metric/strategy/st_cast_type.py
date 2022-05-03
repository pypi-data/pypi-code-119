"""
   Descp: Strategy pattern to create a 'votes by type' metric.

   Created on: 21-oct-2020

   Copyright 2020-2021 Youssef 'FRYoussef' El Faqir El Rhazoui
        <f.r.youssef@hotmail.com>
"""
import pandas as pd
from typing import List

from dao_analyzer.apps.common.data_access.daos.metric.strategy import IMetricStrategy
from dao_analyzer.apps.common.business.transfers.stacked_serie import StackedSerie
from dao_analyzer.apps.common.business.transfers.serie import Serie
import dao_analyzer.apps.common.data_access.pandas_utils as pd_utl


class StCastType(IMetricStrategy):
    __DF_DATE = 'createdAt'
    __DF_COUNT = 'count'
    __DF_SUPPORT = 'supports'
    __DF_COLS = [__DF_DATE, __DF_SUPPORT]


    def clean_df(self, df: pd.DataFrame) -> pd.DataFrame:
        dff: pd.DataFrame = df
        dff.loc[:, self.__DF_COLS] = dff[self.__DF_COLS]
        return dff


    def process_data(self, df: pd.DataFrame) -> StackedSerie:
        if pd_utl.is_an_empty_df(df):
            return StackedSerie()

        df = self.clean_df(df=df)
        
        # takes just the month
        df = pd_utl.unix_to_date(df, self.__DF_DATE)
        df = pd_utl.transform_to_monthly_date(df, self.__DF_DATE)

        df = pd_utl.count_cols_repetitions(df, self.__DF_COLS, self.__DF_COUNT)
        
        # generates a time series
        idx = pd_utl.get_monthly_serie_from_df(df, self.__DF_DATE)
        dff = pd_utl.get_df_from_lists([idx, 0], [self.__DF_DATE, self.__DF_COUNT])
        dff = pd_utl.datetime_to_date(dff, self.__DF_DATE)

        serie: Serie = Serie(x=dff[self.__DF_DATE].tolist())
        positives: List = self.__get_outcome(True, df, dff)
        negatives: List = self.__get_outcome(False, df, dff)

        metric: StackedSerie = StackedSerie(
            serie = serie, 
            y_stack = [negatives, positives])

        return metric


    def __get_outcome(self, positive: bool, df: pd.DataFrame, 
    dff: pd.DataFrame) -> List[int]:

        d3f: pd.DataFrame = pd_utl.filter_by_col_value(
            df=df, 
            col=self.__DF_SUPPORT, 
            value=positive,
            filters=[pd_utl.EQ])

        d3f = d3f.drop(columns=[self.__DF_SUPPORT])
        d3f = pd.concat([d3f, dff], ignore_index=True)
        d3f = d3f.drop_duplicates(subset=self.__DF_DATE, keep="first")
        d3f = d3f.sort_values(self.__DF_DATE)

        return d3f[self.__DF_COUNT].tolist()
