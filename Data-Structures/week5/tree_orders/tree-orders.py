# python3

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrderTraversal(self, nodes, index):
        nidx = nodes[index]
        if nidx == -1 or len(self.key) < index:
            return
        self.inOrderTraversal(self.left, nidx)
        self.result.append(self.key[nidx])
        self.inOrderTraversal(self.right, nidx)

    def inOrder(self):
        self.result = []
        if len(self.key):
            self.inOrderTraversal(self.left, 0)
            self.result.append(self.key[0])
            self.inOrderTraversal(self.right, 0)
        return self.result

    def preOrderTraversal(self, nodes, index):
        nidx = nodes[index]
        if nidx == -1 or len(self.key) < index:
            return
        self.result.append(self.key[nidx])
        self.preOrderTraversal(self.left, nidx)
        self.preOrderTraversal(self.right, nidx)

    def preOrder(self):
        self.result = []
        if len(self.key):
            self.result.append(self.key[0])
            self.preOrderTraversal(self.left, 0)
            self.preOrderTraversal(self.right, 0)
        return self.result

    def postOrderTraversal(self, nodes, index):
        nidx = nodes[index]
        if nidx == -1 or len(self.key) < index:
            return
        self.postOrderTraversal(self.left, nidx)
        self.postOrderTraversal(self.right, nidx)
        self.result.append(self.key[nidx])

    def postOrder(self):
        self.result = []
        if len(self.key):
            self.postOrderTraversal(self.left, 0)
            self.postOrderTraversal(self.right, 0)
            self.result.append(self.key[0])
        return self.result

    def breadFirst(self):
        que = []
        que.append(0)
        while len(que):
            idx = que.pop(0)
            print self.key[idx]
            if self.left[idx] != -1:
                que.append(self.left[idx])
            if self.right[idx] != -1:
                que.append(self.right[idx])

DEBUG = True


def main():
    if DEBUG:
        with open('test') as inputfile:
            sys.stdin = inputfile
            tree = TreeOrders()
            tree.read()
            print(" ".join(str(x) for x in tree.inOrder()))
            print(" ".join(str(x) for x in tree.preOrder()))
            print(" ".join(str(x) for x in tree.postOrder()))
            tree.breadFirst()
    else:
        tree = TreeOrders()
        tree.read()
        print(" ".join(str(x) for x in tree.inOrder()))
        print(" ".join(str(x) for x in tree.preOrder()))
        print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
