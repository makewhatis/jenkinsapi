import mock
import unittest

from jenkinsapi.jenkins import Jenkins
from jenkinsapi.executors import Executors
from jenkinsapi.executor import Executor


class TestExecutor(unittest.TestCase):

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
          "numExecutors" : 6,
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

    @mock.patch.object(Jenkins, '_poll')
    @mock.patch.object(Executors, '_poll')
    def setUp(self, _poll_executors, _poll_jenkins):
        _poll_jenkins.return_value = self.DATA0
        _poll_executors.return_value = self.DATA1

        # def __init__(self, baseurl, nodename, jenkins_obj):

        self.J = Jenkins('http://localhost:8080')
        self.ns = self.J.get_executors(self.DATA0['displayName'])
        # self.ns = Nodes('http://localhost:8080/computer', 'bobnit', self.J)

    def testRepr(self):
        # Can we produce a repr string for this object
        repr(self.ns)

    def testCheckURL(self):
        self.assertEquals(self.ns.baseurl, 'http://localhost:8080/computer')

    @mock.patch.object(Executor, '_poll')
    def testGetMasterNode(self, _poll_executor):
        _poll_executor.return_value = self.DATA2
        mn = self.ns['master']
        self.assertIsInstance(mn, Executor)

    @mock.patch.object(Executor, '_poll')
    def testGetNonMasterNode(self, _poll_executor):
        _poll_executor.return_value = self.DATA3
        mn = self.ns['halob']
        self.assertIsInstance(mn, Executor)

if __name__ == '__main__':
    unittest.main()
