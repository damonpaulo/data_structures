# from: https://www.techiedelight.com/disjoint-set-data-structure-union-find-algorithm/
class DisjointSet:
    parent = {}
 
    # perform MakeSet operation
    def makeSet(self, universe):
 
        # create `n` disjoint sets (one for each item)
        for i in universe:
            self.parent[i] = i
 
    # Find the root of the set in which element `k` belongs
    def Find(self, k):
 
        # if `k` is root
        if self.parent[k] == k:
            return k
        # recur for the parent until we find the root
        return self.Find(self.parent[k])
 
    # Perform Union of two subsets
    def Union(self, a, b):
 
        # find the root of the sets in which elements
        # `x` and `y` belongs
        x = self.Find(a)
        y = self.Find(b)
 
        self.parent[x] = y
