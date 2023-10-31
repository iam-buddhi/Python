import sys
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        #(1). Construct Graph
        #one dimension with elements to be list
        graph = [[] for _ in xrange(n)] 
        for s,e,w in flights:
            graph[s].append((e,w))
        #(2) Graph Algorithm
        q= [(src,0)] #stop and price
        count = 0
        min_price= sys.maxint #record the minimum price so far
        while q:
            next_stops = []
            for cur, acc_price in q: #same level
                for end,price in graph[cur]:
                    #conditional satisfied, save the price
                    if end==dst:
                        min_price = min(min_price, acc_price+price)
                    #(4) Cut down the complexity 
                    #Instead of directly add the next stop, we only add those stops that have less accumulated price 
                    if min_price>acc_price+price:                 
                        next_stops.append((end,acc_price+price) )
            #(4) Instead of directly add the next stop, we only add those stops that have
            if count==K:
                if min_price<sys.maxint:
                    return min_price
                else:
                    return -1
            q=next_stops[:]
            count+=1
        # this is important too
        if count<=K:
                if min_price<sys.maxint:
                    return min_price
                else:
                    return -1
