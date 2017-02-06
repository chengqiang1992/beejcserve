"""
PYTHON: A QUICK INTRODUCTION TO THE CONCURRENT.FUTURES MODULE

The concurrent.futures modules is part of the standard library which provides level API for launching async task. We
will discuss and go through code samples for the common usages of this module.

Executors
    This module features the Executor class which is an abstract class and it can not be used directly. However it has
    two very useful concrete subclasses - ThreadPoolExecutor and ProcessPoolExecutor. As their names suggest, one uses
    multi threading and the other one uses multi-processing. In both case, we get a pool of threads or processes and we
    can submit tasks to this pool. The pool would assign tasks to the available resources (threads or pools) adn
    schedule them to run.

    ThreadPoolExecutor
        Let's first see some codes:
            _____________________________________________________________
            from concurrent.futures import ThreadPoolExecutor
            from time import sleep
            def return_after_5_secs(message):
                sleep(5)
                return message

            pool = ThreadPoolExecutor(3)
            future = pool.submit(return_after_5_secs, ("hello"))
            print(future.done())
            sleep(5)
            print(future.done())
            print(future.result())
            -------------------------------------------------------------
        I hope the code is pretty self explanatory. We first construct a ThreadPoolExecutor with the number of threads
        we want in the pool. By default the number is 5 we chose to use 3 just because we can ;-). Then we submitted a
        task to the thread pool executor which waits 5 seconds before returning the message it gtes as it's first
        argument. When we submit() a task, we gte back a Future. As we can see in the docs, the Future objects has a
        method - done() which tells us if the future has resolved, that is a value has been set for that particular
        future object. When a task finishes (returns a value or is interrupted by an exception), the thread pool
        executor sets the value to the future object.

        In our example, the task doesn't complete until 5 seconds, so the first call to done() will return False. We
        take a really short nap for 5 secs and then it's done. We can get the result of the future by calling the
        result() method on it.

        A good understanding of the Future object and knowing it's methods would be really beneficial for understanding
        and doing async programming in Python. So i highly recommend taking the time read through the docs.

    ProcessPoolExecutor
        The process pool executor has a very similar API. So let’s modify our previous example and use ProcessPool
        instead:
            _____________________________________________________________
            from concurrent.futures import ProcessPoolExecutor
            from time import sleep
            def return_after_5_secs(message):
                sleep(5)
                return message
            pool = ProcessPoolExecutor(3)
            future = pool.submit(return_after_5_secs, ("hello"))
            print(future.done())
            sleep(5)
            print(future.done())
            print("Result: " + future.result())
            -------------------------------------------------------------
        It works perfectly! But of course, we would want to sue the ProcessPoolExecutor for CPU intensive tasks. The
        ThreadPoolExecutor is better suited for network operations or I/O

        While the API is similar, we must remember that the ProcessPoolExecutor uses the multiprocessing module and is
        not affected by the Global Interpreter Lock. However, we can not use any objects that is not pickable. So we
        need to carefully choose what use/return inside the callable passed to process pool executor.

    Executor.map()
        Both executors have a common method - map(). Like the built in function, then map method allows multiple calls to
        a provided function, passing each of the items in an iterable to that function. Except, in this case, the
        functions are called concurrently. For multiprocessing, this iterable is broken into chunks and each of these
        chunks is passed to the function in separate processes. We can controls the chunks size by passing a third
        parameter, chunk_size. By default the chunk size is 1.

        Here’s the ThreadPoolExample from the official docs:
            __________________________________________________________________________________
            import concurrent.futures
            import urllib.request
            URLS = ['http://www.foxnews.com/',
                    'http://www.cnn.com/',
                    'http://europe.wsj.com/',
                    'http://www.bbc.co.uk/',
                    'http://some-made-up-domain.com/',
                    'http://www.baidu.com/',
                    'http://www.taobao.com/',
                    'http://www.tamll.com/',
                    'http://www.jd.com/']
            # Retrieve a single page and report the url and contents
            def load_url(url, timeout):
                with urllib.request.urlopen(url, timeout=timeout) as conn:
                    return conn.read()
            # We can use a with statement to ensure threads are cleaned up promptly
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
                for future in concurrent.futures.as_completed(future_to_url):
                    url = future_to_url[future]
                    try:
                        data = future.result()
                    except Exception as exc:
                        print('%r generated an exception: %s' % (url, exc))
                    else:
                        print('%r page is %d bytes' % (url, len(data)))
            ---------------------------------------------------------------------------------

        And the ProcessPoolExecutor example:
            ___________________________________________________________________________________
            import concurrent.futures
            import math
            PRIMES = [
                112272535095293,
                112582705942171,
                112272535095293,
                115280095190773,
                115797848077099,
                1099726899285419]
            def is_prime(n):
                if n % 2 == 0:
                    return False
                sqrt_n = int(math.floor(math.sqrt(n)))
                for i in range(3, sqrt_n + 1, 2):
                    if n % i == 0:
                        return False
                return True
            def main():
                with concurrent.futures.ProcessPoolExecutor() as executor:
                    for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
                        print('%d is prime: %s' % (number, prime))
            if __name__ == '__main__':
                main()
            ------------------------------------------------------------------------------------

"""

import concurrent.futures
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))

if __name__ == '__main__':
    main()







