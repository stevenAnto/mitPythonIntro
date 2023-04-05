class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self._name = name
    def get_name(self):
        return self._name
    def __str__(self):
        return self._name


class Edge(object):
    def __init__(self, src, dest):
        """Assumes
        src and dest are nodes"""
        self._src = src
        self._dest= dest
    def get_source(self):
        return self._src
    def get_destination(self):
        return self._dest
    def __str__(self):
        return self._src.get_name()+'->'+self.dest.get_name()

class Weighted_edge(Edge):
    def __init__(self, src, dest, weight =1.0):
        """Assumes src and des are nodes, weight is a number"""
        self._src =src
        self._dest = dest
        self._weight = weight
    def get_weight(self):
        return self._weight
    def __str__(self):
        return (f'{self._src.get_name()}-->({self._weight})'+f'{self._dest.get_name()}')
