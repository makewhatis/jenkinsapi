import mock
import types
import unittest

from jenkinsapi.jenkins import Jenkins
from jenkinsapi.executors import Executors
from jenkinsapi.executor import Executor


class TestExecutors(unittest.TestCase):

    DATAM = {
        'assignedLabels': [{}],
        'description': None,
        'jobs': [],
        'mode': 'NORMAL',
        'nodeDescription': 'the master Jenkins node',
        'nodeName': '',
        'numExecutors': 2,
        'overallLoad': {},
        'primaryView': {'name': 'All', 'url': 'http://localhost:8080/'},
        'quietingDown': False,
        'slaveAgentPort': 0,
        'unlabeledLoad': {},
        'useCrumbs': False,
        'useSecurity': False,
        'views': [
            {'name': 'All', 'url': 'http://localhost:8080/'},
            {'name': 'BigMoney', 'url': 'http://localhost:8080/view/BigMoney/'}
        ]
    }

    DATA0 = {
          "actions" : [
            
          ],
          "displayName" : "host0.host.com",
          "executors" : [
            {
              
            },
            {
              
            },
            {
              
            },
            {
              
            },
            {
              
            },
            {
              
            },
            {
              
            },
            {
              
            }
          ],
          "icon" : "computer.png",
          "idle" : False,
          "jnlpAgent" : True,
          "launchSupported" : False,
          "loadStatistics" : {
            
          },
          "manualLaunchAllowed" : True,
          "monitorData" : {
            "hudson.node_monitors.SwapSpaceMonitor" : {
              "availablePhysicalMemory" : 8462417920,
              "availableSwapSpace" : 0,
              "totalPhysicalMemory" : 75858042880,
              "totalSwapSpace" : 0
            },
            "hudson.node_monitors.ArchitectureMonitor" : "Linux (amd64)",
            "hudson.node_monitors.ResponseTimeMonitor" : {
              "average" : 2
            },
            "hudson.node_monitors.TemporarySpaceMonitor" : {
              "path" : "/tmp",
              "size" : 430744551424
            },
            "hudson.node_monitors.DiskSpaceMonitor" : {
              "path" : "/data/jenkins",
              "size" : 1214028627968
            },
            "hudson.node_monitors.ClockMonitor" : {
              "diff" : 1
            }
          },
          "numExecutors" : 8,
          "offline" : False,
          "offlineCause" : None,
          "offlineCauseReason" : "",
          "oneOffExecutors" : [
            {
              
            },
            {
              
            }
          ],
          "temporarilyOffline" : False
        }

    DATA1 = {
          "actions" : [
            
          ],
          "displayName" : "host1.host.com",
          "executors" : [
            {
              
            },
            {
              
            }
          ],
          "icon" : "computer.png",
          "idle" : False,
          "jnlpAgent" : True,
          "launchSupported" : False,
          "loadStatistics" : {
            
          },
          "manualLaunchAllowed" : True,
          "monitorData" : {
            "hudson.node_monitors.SwapSpaceMonitor" : {
              "availablePhysicalMemory" : 8462417920,
              "availableSwapSpace" : 0,
              "totalPhysicalMemory" : 75858042880,
              "totalSwapSpace" : 0
            },
            "hudson.node_monitors.ArchitectureMonitor" : "Linux (amd64)",
            "hudson.node_monitors.ResponseTimeMonitor" : {
              "average" : 2
            },
            "hudson.node_monitors.TemporarySpaceMonitor" : {
              "path" : "/tmp",
              "size" : 430744551424
            },
            "hudson.node_monitors.DiskSpaceMonitor" : {
              "path" : "/data/jenkins",
              "size" : 1214028627968
            },
            "hudson.node_monitors.ClockMonitor" : {
              "diff" : 1
            }
          },
          "numExecutors" : 2,
          "offline" : False,
          "offlineCause" : None,
          "offlineCauseReason" : "",
          "oneOffExecutors" : [
            {
              
            },
            {
              
            }
          ],
          "temporarilyOffline" : False
        }

    DATA2 = {
          "actions" : [
            
          ],
          "displayName" : "host2.host.com",
          "executors" : [
            {
              
            },
            {
              
            },
            {
              
            },
            {
              
            }
          ],
          "icon" : "computer.png",
          "idle" : False,
          "jnlpAgent" : True,
          "launchSupported" : False,
          "loadStatistics" : {
            
          },
          "manualLaunchAllowed" : True,
          "monitorData" : {
            "hudson.node_monitors.SwapSpaceMonitor" : {
              "availablePhysicalMemory" : 8462417920,
              "availableSwapSpace" : 0,
              "totalPhysicalMemory" : 75858042880,
              "totalSwapSpace" : 0
            },
            "hudson.node_monitors.ArchitectureMonitor" : "Linux (amd64)",
            "hudson.node_monitors.ResponseTimeMonitor" : {
              "average" : 2
            },
            "hudson.node_monitors.TemporarySpaceMonitor" : {
              "path" : "/tmp",
              "size" : 430744551424
            },
            "hudson.node_monitors.DiskSpaceMonitor" : {
              "path" : "/data/jenkins",
              "size" : 1214028627968
            },
            "hudson.node_monitors.ClockMonitor" : {
              "diff" : 1
            }
          },
          "numExecutors" : 4,
          "offline" : False,
          "offlineCause" : None,
          "offlineCauseReason" : "",
          "oneOffExecutors" : [
            {
              
            },
            {
              
            }
          ],
          "temporarilyOffline" : False
        }

    DATA3 = {
          "actions" : [
            
          ],
          "displayName" : "host3.host.com",
          "executors" : [
            {
              
            }
          ],
          "icon" : "computer.png",
          "idle" : False,
          "jnlpAgent" : True,
          "launchSupported" : False,
          "loadStatistics" : {
            
          },
          "manualLaunchAllowed" : True,
          "monitorData" : {
            "hudson.node_monitors.SwapSpaceMonitor" : {
              "availablePhysicalMemory" : 8462417920,
              "availableSwapSpace" : 0,
              "totalPhysicalMemory" : 75858042880,
              "totalSwapSpace" : 0
            },
            "hudson.node_monitors.ArchitectureMonitor" : "Linux (amd64)",
            "hudson.node_monitors.ResponseTimeMonitor" : {
              "average" : 2
            },
            "hudson.node_monitors.TemporarySpaceMonitor" : {
              "path" : "/tmp",
              "size" : 430744551424
            },
            "hudson.node_monitors.DiskSpaceMonitor" : {
              "path" : "/data/jenkins",
              "size" : 1214028627968
            },
            "hudson.node_monitors.ClockMonitor" : {
              "diff" : 1
            }
          },
          "numExecutors" : 1,
          "offline" : False,
          "offlineCause" : None,
          "offlineCauseReason" : "",
          "oneOffExecutors" : [
            {
              
            },
            {
              
            }
          ],
          "temporarilyOffline" : False
        }


    EXEC0 = {
      "currentExecutable" : {
        "number" : 4168,
        "url" : "http://localhost:8080/job/testjob/4168/"
      },
      "currentWorkUnit" : {
        
      },
      "idle" : False,
      "likelyStuck" : False,
      "number" : 0,
      "progress" : 48
    }

    @mock.patch.object(Jenkins, '_poll')
    @mock.patch.object(Executors, '_poll')
    def setUp(self, _poll_executor, _poll_jenkins):
        _poll_jenkins.return_value = self.DATAM
        _poll_executor.return_value = self.DATA0
        self.J = Jenkins('http://localhost:8080')
        self.executors = self.J.get_executors(self.DATA0['displayName'])
        # self.ns = Nodes('http://localhost:8080/computer', 'bobnit', self.J)

    def testRepr(self):
        # Can we produce a repr string for this object
        repr(self.J)

    def testCheckURL(self):
        self.assertEquals(self.J.baseurl, 'http://localhost:8080')

    @mock.patch.object(Jenkins, '_poll')
    @mock.patch.object(Executors, '_poll')
    @mock.patch.object(Executor, '_poll')
    def testGetExecutors(self, _poll_executor, _poll_executors, _poll_jenkins):
        _poll_jenkins.return_value = self.DATAM
        _poll_executor.return_value = self.EXEC0
        _poll_executors.return_value = self.DATA3
        exec_info = self.J.get_executors(self.DATA3['displayName'])

        self.assertIsInstance(exec_info, object)
        for e in exec_info:
            self.assertEquals(e.get_progress(), 48, 'Should return 48 %')


if __name__ == '__main__':
    unittest.main()
