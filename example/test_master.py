from Pikka.Pikka import Pikka


def main():
    jkka = Pikka(actions={}, host='localhost', port=9000, master=True)
    """
    time.sleep(10)
    jkka.message('ECHO', num=1)
    time.sleep(3)
    jkka.message('ECHO', num=1)
    time.sleep(3)
    jkka.message('ECHO', num=1)
    time.sleep(3)
    """

if __name__ == "__main__":
    main()