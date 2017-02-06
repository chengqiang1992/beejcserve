"""
Asynchronous and non-Blocking I/O

Real-time web features require a long-lived mostly-idle connection per user. In a traditional synchronous web server,
this implies devoting one thread to each other, which can be very expensive.

To minimize the cost of concurrent connection, Tornado uses a single thread event loop. This means that all application
code should aim to be asynchronous and non-blocking because only one operation can be at a time.

The terms asynchronous and non-blocking are closely related and are often used interchangeably, but they are not quite
the same thing.


    Blocking
        A function blocks when it waits for something to happen before returning.

    Asynchronous
        An asynchronous function returns before it is finished, and generally causes some work to happen in the
        background before trigger some future action in the application.

        - Callback argument
        - Return a placeholder(Future, Promise, Deferred)
        - Deliver to a queue
        - Callback registry(e.g. POSIX signals)

    Example

        Herr is a sample synchronous function:
            _________________________________________________
            from tornado.httpclient import HTTPClient
            def synchronous_fetch(url):
                http_client = HTTPClient()
                response = http_client.fetch(url)
                return response
            -------------------------------------------------

        And here is the same function rewritten to be asynchronous with a callback argument:
             _________________________________________________
            from tornado.httpclient import AsyncHTTPClient
            def asynchronous_fetch(url, callback):
                http_client = AsyncHTTPClient()
                def handle_response(response):
                    callback(response.body)
                http_client.fetch(url, callback=handle_response)
            -------------------------------------------------


"""




