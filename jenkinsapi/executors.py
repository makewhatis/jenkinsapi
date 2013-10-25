"""
This module implements the Executors class, which is intended to be a container-like
interface for all of the executors defined on a single Jenkins node.
"""
import logging
from jenkinsapi.executor import Executors
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



    def __str__(self):
        return 'Nodes @ %s' % self.baseurl

    def __contains__(self, nodename):
        return nodename in self.keys()

    def iterkeys(self):
        for item in self._data['computer']:
            yield item['displayName']

    def keys(self):
        return list(self.iterkeys())

    def iteritems(self):
        for item in self._data['computer']:
            nodename = item['displayName']
            if nodename.lower() == 'master':
                nodeurl = '%s/(%s)' % (self.baseurl, nodename)
            else:
                nodeurl = '%s/%s' % (self.baseurl, nodename)
            try:
                yield item['displayName'], Node(nodeurl, nodename, self.jenkins)
            except Exception:
                import ipdb
                ipdb.set_trace()

    def __getitem__(self, nodename):
        self_as_dict = dict(self.iteritems())
        if nodename in self_as_dict:
            return self_as_dict[nodename]
        else:
            raise UnknownNode(nodename)

    def __len__(self):
        return len(self.iteritems())