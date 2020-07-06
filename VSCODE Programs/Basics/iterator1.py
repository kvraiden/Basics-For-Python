class InfIter:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        num = self.num
        self.num += 2
        return num
i = InfIter()
a = iter(i)

for x in a:
    if next(a)<=1000:
        print(next(a))