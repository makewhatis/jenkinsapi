"""
This module implements the Executors class, which is intended to be a container-like
interface for all of the executors defined on a single Jenkins node.
"""
import logging
from jenkinsapi.executor import Executor
from jenkinsapi.custom_exceptions import JenkinsAPIException, UnknownExecutor
from jenkinsapi.jenkinsbase import JenkinsBase

log = logging.getLogger(__name__)


class Executors(JenkinsBase):
    """
    This class provides a container-like API which gives
    access to all executors on a Jenkins node. It behaves
    like a list, where executors are accessed via index number.
    """
    def __init__(self, baseurl, nodename, jenkins):
        self.nodename = nodename
        self.jenkins = jenkins
        JenkinsBase.__init__(self, baseurl)
        self.count = len(self._data['executors'])

    def __str__(self):
        return 'Executors @ %s' % self.baseurl

    def __iter__(self):
        for index in range(self.count):
            str(index)
            executor_url = '%s/executors/%s' % (self.baseurl, index)
            try:
                yield Executor(executor_url, self.nodename, self.jenkins, index)
            except JenkinsAPIException as e:
                log.error("Error querying Executors: %s" % e)

                

