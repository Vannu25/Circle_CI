from main import add


class Test1:
    def testAdd(self):
        assert add(2, 3) == 5
        print('The add function works properly')