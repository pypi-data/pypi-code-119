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

from autoai_ts_libs.deps.tspy.data_structures.ml.clustering.KShapeModel import KShapeModel


class Factory(object):

    def __init__(self, tsc):
        self._tsc = tsc

    def load(self, path):

        # todo this will need changing since str does not always imply it should be FileInputStream
        if isinstance(path, str):
            j_model = self._tsc._jvm.com.ibm.research.time_series.ml.clustering.k_shape.containers.KShapeModel.load(
                self._tsc._jvm.java.io.FileInputStream(path)
            )
        else:
            j_model = self._tsc._jvm.com.ibm.research.time_series.ml.clustering.k_shape.containers.KShapeModel.load(path)

        return KShapeModel(self._tsc, j_model)

