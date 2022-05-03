"""
   Descp: This class is used to adapt installed apps metrics.

   Created on: 20-oct-2020

   Copyright 2020-2021 Youssef 'FRYoussef' El Faqir El Rhazoui
        <f.r.youssef@hotmail.com>
"""

from typing import Dict, List, Callable

import dao_analyzer.apps.common.resources.colors as Color
from dao_analyzer.apps.common.business.transfers.stacked_serie import StackedSerie
from dao_analyzer.apps.common.business.transfers.organization import OrganizationList
from dao_analyzer.apps.common.business.i_metric_adapter import IMetricAdapter
import dao_analyzer.apps.aragon.data_access.daos.metric.\
    metric_dao_factory as s_factory

class InstalledApps(IMetricAdapter):

    def __init__(self, organizations: Callable[...,OrganizationList]) -> None:
        self.__organizations = organizations


    @property
    def organizations(self) -> OrganizationList:
        return self.__organizations()

    def get_plot_data(self, o_id: str) -> Dict:
        """
        Returns the metric data in a Dict using o_id param.
        """
        dao = s_factory.get_dao(
            ids=self.organizations.get_ids_from_id(o_id),
            metric=s_factory.INSTALLED_APPS
        )
        metric: StackedSerie = dao.get_metric()

        y: List[float] = metric.get_i_stack(0)
        color = [Color.LIGHT_BLUE] * len(y)

        return {
            'x': metric.get_serie(),
            'y': y,
            'name': '',
            'color': color,
            'type': 'category',
            'x_format': '',
            'last_serie_elem': '',
            'last_value': '',
            'diff': '',
        }
