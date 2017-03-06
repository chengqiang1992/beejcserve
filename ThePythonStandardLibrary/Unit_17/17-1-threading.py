"""
17. Concurrent Execution
    The modules described in this chapter provide support for concurrent execution of code. The appropriate choice of
    tool will depend on the task to be executed (CPU bound bs IO bound) and preferred style of development (event driven
    cooperative multitasking vs preemptive multitasking). Here's an overview.

    在这章中，这个模块提供并发执行的代码。对于工具的适当选择将取决于 任务执行 CPU绑定和IO绑定 首要开发风格 事件驱的协作
    多任务 和 抢占式多任务

    17.3. The concurrent package
        Currently, there is only one module in this package:
            concurrent.futures -- Launching parallel tasks 启动并行任务

    17.4. concurrent.futures -- Launching parallel tasks
        New in version 3.2
        Source code:

        The concurrent.futures module provides a high-level interface for asynchronously executing callables.

        The asynchronous execution can be performed with threads, using ThreadPoolExecutor, or separate process, using
        ProcessPoolExecutor. Both implement the same interface, which is defined by the abstract Executor class.

        17.4.1. Executor Objects
            class concurrent.futures.Executor
                An abstract class that provides methods to execute calls asynchronously. It should not be used directly,
                but through its concurrent subclasses.

                    submit(fn, *args, **kwargs)
                        Schedules the callable, fn, to be executed as fn(*args **kwargs) and returns a Future Object
                        representing the execution of the callable.
                        _________________________________________________________________
                        |    with futures.ThreadPoolExecutor(max_workers=1) as executor: |
                        |    futures = executor.submit(pow, 323, 12350)                  |
                        |   print(futures.result())                                      |
                        -----------------------------------------------------------------

                    map(func, *iterable, timeout=None, chunksize=1)
                        Equivalent to map(func, *iterables) except func is executed asynchronously and several calls to
                        func may be made concurrently. The returned iterator raises a concurrent.futures.TimeoutError if
                        __next__() is called and the result isn’t available after timeout seconds from the original call
                        to Executor.map(). timeout can be an int or a float. If timeout is not specified or None, there
                        is no limit to the wait time. If a call raises an exception, then that exception will be raised
                        when its value is retrieved from the iterator. When using ProcessPoolExecutor, this method chops
                        iterables into a number of chunks which it submits to the pool as separate tasks. The (approximate)
                        size of these chunks can be specified by setting chunksize to a positive integer. For very long
                        iterables, using a large value for chunksize can significantly improve performance compared to
                        the default size of 1. With ThreadPoolExecutor, chunksize has no effect.

                    shutdown(wait=True)
                        Signal the executor that is should free an resources that it is using when the currently pending
                        futures are done executing. Calls to Executor.submit() abd Executor.map() made after shutdown will
                        raise RuntimeError.

                        If wait is True then this method will not return until all the pending futures are done executing
                        and the resources

        17.4.2. ThreadPoolExecutor
            ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously.

            DeadLocks can occur when the callable associated with a Future waits on the results of another Future.
            For example:
            _______________________________________________________________________________________
                import time
                from concurrent import futures

                def wait_on_b():
                    time.sleep(5)
                    print(b.result())         b will never complete because it is waiting on a.
                    return 5

                def wait_on_a():
                    time.sleep(5)
                    print(a.result())          a will never complete because it is waiting on b.
                    return 6

                executor = futures.ThreadPoolExecutor(max_workers=2)
                a = executor.submit(wait_on_a)
                b = executor.submit(wait_on_b)
            --------------------------------------------------------------------------------------

            class concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix='')
                An Executor subclass that uses a pool of most_workers threads to execute calls asynchronously.
                Changed in version 3.5: if max_workers is None or not given, it will default to the number of processors
                on the machine, multiplied by 5, assuming that ThreadPoolExecutor is often used to overlap I/O instead
                of CPU work and the number of workers should be higher than the number of workers for ProcessPoolExecutor.

                GIL的特性，也就导致了python不能充分利用多核cpu。而对面向I/O的（会调用内建操作系统C代码的）程序来说，GIL
                会在这个I/O调用之前被释放，以允许其他线程在这个线程等待I/O的时候运行。如果线程并为使用很多I/O操作，它会
                在自己的时间片一直占用处理器和GIL。这也就是所说的：I/O密集型python程序比计算密集型的程序更能充分利用多线
                程的好处。
                总之，不要使用python多线程，使用python多进程进行并发编程，就不会有GIL这种问题存在，并且也能充分利用多核cpu。

                New in version 3.6: The thread_name_prefix argument was added to allow users to control the threading.
                Thread names for worker threads created by the pool for easier debugging.

                17.4.2.1. ThreadPoolExecutor Example
"""


# import time
# from concurrent import futures
#
#
# def wait_on_b():
#     print(5)
#     time.sleep(5)
#
#
# def wait_on_a():
#     print(6)
#     time.sleep(6)
#
#
# executor = futures.ThreadPoolExecutor(max_workers=2)
# executor.submit(wait_on_a)
# executor.submit(wait_on_b)


import concurrent.futures
import urllib.request


URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']


# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


# we can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))


