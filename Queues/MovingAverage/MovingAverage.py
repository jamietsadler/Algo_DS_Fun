
class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.size:
            self.queue.pop(0)
        self.queue.append(val)
        
        return sum(self.queue)/float(len(self.queue))
        
        
        