
def f(n:int):
    print('in f')
    assert n > 0, 'positive input only'
    return n


def g(n):
    print('in g')
    assert n < 5, 'only accept input less than 5'
    n *= 3
    return n

def h(n):
    print('in h')
    assert n % 2, 'only accept odd input'
    return n


def control0(tasks, x0):
    print(f'input: {x0}')
    for t in tasks:
        x0 = t(x0)
    print(f'final output: {x0}')


def flow(x0):
    print(f'input: {x0}')
    try:
        while True:
            task = yield
            x0 = task(x0)
    except GeneratorExit:
        print(f'final output: {x0}')


# separate the responsibility
def control1(tasks, x0):
    worker = flow(x0)
    next(worker)
    for t in tasks:
        worker.send(t)
    worker.close()  # optional


def flow1(x0, sink):
    print(f'input: {x0}')
    while True:
        task = yield
        x0 = task(x0)
        sink.send(x0)

def sink():
    try:
        while True:
            x = yield
    except GeneratorExit:
        print(f'final output: {x}')

# separate the responsibility further
def control2(tasks, x0):
    post_proc = sink()
    next(post_proc)
    worker = flow1(x0, post_proc)
    next(worker)
    for t in tasks:
        worker.send(t)
#    worker.close()  # optional


if __name__ == '__main__':
    x0 = int(input('Give a number:\n'))
#    control0([f, g, h], x0)
    control2([f, g, h], x0)
