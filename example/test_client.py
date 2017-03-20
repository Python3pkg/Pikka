import time

import Pyro4

from core.singleton.singleton import Singleton
from Pikka import Pikka


class TestCounter(metaclass=Singleton):
    counter = 0


@Pyro4.expose
class test_echo():

    def message(self, num):
        TestCounter().counter += num
        print("counter: {}".format(TestCounter().counter))
        return TestCounter().counter


def main():
    jkka = Pikka(host='localhost',
                 port=9001,
                 actions={'ECHO': test_echo})


if __name__ == "__main__":
    main()