"""
Created on Dec 4, 2023

@author: CyberiaResurrection

Encapsulate all the mod-XML-file gubbins here, as a single point of truth on the way in from and out to the
raw XML, so no one else has to worry
"""
from defusedxml.ElementTree import parse


class ModFileReader(object):

    def __init__(self, filename):
        self.filename = filename
        self.modfile = parse(self.filename)
        assert self.modfile is not None, "XML not parsed"
