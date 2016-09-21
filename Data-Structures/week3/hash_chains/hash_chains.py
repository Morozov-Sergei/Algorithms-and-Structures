# python3
from collections import OrderedDict as OD

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):

        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(list(self.elems.get(query.ind,dict()).keys())))
        else:
            key = self._hash_func(query.s)
            if query.type == 'find':
                self.write_search_result(key in self.elems and query.s in self.elems[key])
            elif query.type == 'add':
                if key in self.elems:
                    self.elems[key][query.s] = query.s
                else:
                    self.elems[key]= OD({query.s:query.s})
            else:
                if key in self.elems:
                    self.elems[key].pop(query.s, None)

    def process_queries(self):
        if DEBUG:
            n = int(self.inputfile.readline())
            for i in range(n):
                self.process_query(Query(self.inputfile.readline().split()))
        else:
            n = int(input())
            for i in range(n):
                self.process_query(self.read_query())

DEBUG = False

if __name__ == '__main__':
    if DEBUG:
        with open('input') as inputfile:
            bucket_count = int(inputfile.readline())
            proc = QueryProcessor(bucket_count)
            proc.inputfile = inputfile
            proc.process_queries()
    else:
        bucket_count = int(input())
        proc = QueryProcessor(bucket_count)
        proc.process_queries()
