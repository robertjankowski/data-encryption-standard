import os
import random
import threading
import time

from des import DES

d = DES()
input = 'test'
c = d.encrypt(input)[0]


def des_brute_force(key: list):
    d.subkeys = d._prepare_keys(key)
    return d.decrypt(c).strip() == input


def random_key():
    return random.choices([0, 1], k=64)


class Task(threading.Thread):
    def run(self):
        print('Starting {}'.format(self.name))
        start = time.time()
        while True:
            r_k = random_key()
            if des_brute_force(r_k):
                end = time.time()
                print('Found key: {}'.format(r_k))
                print('Elapsed: {}s'.format(end - start))
                os._exit(1)


if __name__ == '__main__':
    tasks = []
    for _ in range(4):
        t = Task()
        t.start()
        tasks.append(t)
    [t.join() for t in tasks]
