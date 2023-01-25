class Recursion:
    def __init__(self):
        self.count = 0

    def simpleRecursion(self, n):
        self.count += 1
        print("Count: ", self.count)
        if n == 0:
            return
        else:
            self.simpleRecursion(n - 1)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)
