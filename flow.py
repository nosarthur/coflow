
def target(x0, sink):
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


