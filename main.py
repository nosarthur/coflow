from demo import h, g, f
from flow import target, sink

if __name__ == '__main__':
    x0 = int(input('Give a number:\n'))
    tasks = [f, g, h]

    post_proc = sink()
    next(post_proc)
    worker = target(x0, post_proc)
    next(worker)
    for t in tasks:
        worker.send(t)

