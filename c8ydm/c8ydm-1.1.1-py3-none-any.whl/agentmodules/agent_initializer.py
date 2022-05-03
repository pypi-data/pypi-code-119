#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""  
Copyright (c) 2021 Software AG, Darmstadt, Germany and/or its licensors

SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import logging
import time
from c8ydm.framework.modulebase import Initializer
from c8ydm.framework.smartrest import SmartRESTMessage


class AgentInitializer(Initializer):
    logger = logging.getLogger(__name__)
    agent_message_id = 'dm200'
    xid = 'c8y-dm-agent-v1.0'

    def getMessages(self):
        self.logger.info(f'Agent Initializer called...')
        agent_msg = SmartRESTMessage(
            's/uc/'+self.xid, self.agent_message_id, [self.serial, 'DM Reference Agent', '0.2', ''])
        return [agent_msg]
