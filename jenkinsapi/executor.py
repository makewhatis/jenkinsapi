"""
Module for jenkinsapi Executer class
"""

from jenkinsapi.jenkinsbase import JenkinsBase
import logging
import urllib

log = logging.getLogger(__name__)


class Executor(JenkinsBase):
    """
    Class to hold information on nodes that are attached as slaves to the master jenkins instance
    """

    def __init__(self, baseurl, nodename, jenkins_obj, number):
        """
        Init a node object by providing all relevant pointers to it
        :param baseurl: basic url for querying information on a node
        :param nodename: hostname of the node
        :param jenkins_obj: ref to the jenkins obj
        :return: Node obj
        """
        self.nodename = nodename
        self.number = number
        self.jenkins = jenkins_obj
        self.baseurl = baseurl
        JenkinsBase.__init__(self, baseurl)

    def get_jenkins_obj(self):
        return self.jenkins

    def __str__(self):
        return '%s' % self.number

    def get_progress(self):
        """Returns percentage"""
        self.poll()
        return self._data['progress']

    def is_idle(self):
        """
        Returns Boolean
        """
        self.poll()
        return self._data['is_idle']