﻿#  /************** Begin Copyright - Do not add comments here **************
#   * Licensed Materials - Property of IBM
#   *
#   *   OCO Source Materials
#   *
#   *   (C) Copyright IBM Corp. 2020, All Rights Reserved
#   *
#   * The source code for this program is not published or other-
#   * wise divested of its trade secrets, irrespective of what has
#   * been deposited with the U.S. Copyright Office.
#   ***************************** End Copyright ****************************/

import datetime

from autoai_ts_libs.deps.tspy.data_structures.io import PullStreamMultiTimeSeriesReader
from autoai_ts_libs.deps.tspy.data_structures.stream_multi_time_series.StreamMultiTimeSeries import StreamMultiTimeSeries
from autoai_ts_libs.deps.tspy.data_structures import utils
from autoai_ts_libs.deps.tspy.data_structures.observations.TRS import TRS


class Factory:

    def __init__(self, tsc):
        self._tsc = tsc

    def reader(self, stream_reader, granularity=None, start_time=None):

        if isinstance(stream_reader, PullStreamMultiTimeSeriesReader.PullStreamMultiTimeSeriesReader):
            py_reader = utils.JavaPullStreamMultiTimeSeriesReader(stream_reader)
        else:
            py_reader = utils.JavaPushStreamMultiTimeSeriesReader(stream_reader)


        if granularity is None and start_time is None:
            return StreamMultiTimeSeries(
                self._tsc,
                self._tsc._jvm.com.ibm.research.time_series.streaming.timeseries.StreamMultiTimeSeries.reader(py_reader)
            )
        else:
            if granularity is None:
                granularity = datetime.timedelta(milliseconds=1)
            if start_time is None:
                start_time = datetime.datetime(1970, 1, 1, 0, 0, 0, 0)
            trs = TRS(self._tsc, granularity, start_time)
            return StreamMultiTimeSeries(
                self._tsc,
                self._tsc._jvm.com.ibm.research.time_series.streaming.timeseries.StreamMultiTimeSeries.reader(
                    py_reader,
                    trs._j_trs
                ),
                trs
            )

    def text_file(self, path, map_func, granularity=None, start_time=None):

        if granularity is None and start_time is None:
            return StreamMultiTimeSeries(
                self._tsc,
                self._tsc._jvm.com.ibm.research.time_series.streaming.timeseries.StreamMultiTimeSeries.textFile(
                    path,
                    utils.UnaryMapFunctionTupleResultingInOptional(self._tsc, map_func)
                )
            )
        else:
            if granularity is None:
                granularity = datetime.timedelta(milliseconds=1)
            if start_time is None:
                start_time = datetime.datetime(1970, 1, 1, 0, 0, 0, 0)
            trs = TRS(self._tsc, granularity, start_time)

            return StreamMultiTimeSeries(
                self._tsc,
                self._tsc._jvm.com.ibm.research.time_series.streaming.timeseries.StreamMultiTimeSeries.textFile(
                    path,
                    utils.UnaryMapFunctionTupleResultingInOptional(self._tsc, map_func),
                    trs._j_trs
                ),
                trs
            )

    def queue(self, key_observation_queue, granularity=None, start_time=None):
        from autoai_ts_libs.deps.tspy.data_structures.io.PythonQueueStreamMultiTimeSeriesReader import PythonQueueStreamMultiTimeSeriesReader
        return self.reader(PythonQueueStreamMultiTimeSeriesReader(key_observation_queue), granularity, start_time)
