# Copyright (C) 2020 Cuong Tran - cuongtran@mnm-team.org
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'Cuong Ngoc Tran'

from time import sleep

from ryu.base import app_manager
from ryu.controller.handler import set_ev_cls
from ryu.topology import event
from ryu.topology.api import get_switch, get_link, get_host

"""
Instructions:
    ryu-manager --observe-links topo_disc.py
We can also run this with other apps by:
    ryu-manager --observe-links topo_disc.py app1.py app2.py

The GUI version from ryu is under ryu/app/gui_topology/
"""

class test(app_manager.RyuApp):

    def __init__(self, *args, **kwargs):
        super(test, self).__init__(*args, **kwargs)
        self.count = 1

    @set_ev_cls(event.EventSwitchEnter)
    def handler_switch_enter(self, ev):
        print(" " + str(self.count) + " -- Switch: "),
        print(ev.switch)
#        switches_list = get_switch(self, None)
#        index = 1
#        for switch in switches_list:
#            print("\t " + str(index)),
#            print(switch)
#            index += 1

        sleep(0.3) # can change this, this sleeping period helps making the get_link function in the next line work correctly, don't know the reason why. You can comment this line and check if the link discovery still functions correctly.
        links_list = get_link(self, None)
        print(" " + str(self.count) + " -- Links: ")
        index = 1
        for link in links_list:
            print("\t " + str(index)),
            print(link)
            index += 1

#        hosts_list = get_host(self, None)
#        print(" " + str(self.count) + " -- Hosts: ")
#        index = 1
#        for host in hosts_list:
#            print("\t " + str(index)),
#            print(host)
#            index += 1

        self.count += 1
