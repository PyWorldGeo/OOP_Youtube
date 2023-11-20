#ფუნქტორი არის ობიექტი, რომელიც გამოიყენება როგორც ფუნქცია

class Functor:
    def __int__(self, n=15):
        self.n = n

    def __call__(self, x):
        if type(x) is str:
            self.__handle_string(x)
        if type(x) is int:
            self.__handle_integer(x)

    @staticmethod
    def __handle_string(a):
        print("I am handling string", a)

    @staticmethod
    def __handle_integer(a):
        print("I am handling integer", a)


class CallFunctor:
    def __init__(self):
        self.our_obj = Functor()

    def do_something(self, info):
        self.our_obj(info)


call = CallFunctor()
call.do_something(5)