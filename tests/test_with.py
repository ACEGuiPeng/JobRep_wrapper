# -*-coding:utf-8-*-

class A(object):
    def __enter__(self):
        return 3

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting')

if __name__ == '__main__':
    print('before with')
    with A() as x:
        print('start with')
        print(x)
        print('end with')

