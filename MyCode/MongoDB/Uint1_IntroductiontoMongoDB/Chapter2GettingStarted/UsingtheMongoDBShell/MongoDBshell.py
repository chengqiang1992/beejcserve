"""
2.7 使用 MongoDB shell
    本节将介绍如何将shell作为命令行工具的一部分来使用，如果对shell进行钉子，以及shell的一些高级功能。

    在上面的例子中，我们只是连接到了一个本地的 mongod 实例。事实上，可以将shell连接到任何 MongoDB 实例（只要你的计算机
    与MongoDB实例所在的计算机能够连通）。在启动 shell 时指定机器名和端口，就可以链接到一台不同的机器（或者端口）:
        $ mongo some-host:3000/mtDB

    db 现在就指向了 some-hots:3000 上的 myDB 数据库。

    2.7.1 shell 小贴士
        由于 mongo 是一个简化的 JavaScript shell，可以通过查看 JavaScript 的在线文档得到大量帮助。对于 MongoDB特有的功能
        ，shell内置了帮助文档，可以使用help命令来查看:
            > help
                de.help()
                db.mycoll.help()
                ...
        如果想知道一个函数是做什么用的，可以直接在shell输入函数名（函数名后不要输入小括号）。
            > db.foo.update
            function (query, obj, upsert, multi) {
                assert(query, "need a query");
            }

    2.7.2 使用 shell 执行脚本
        本书其他章都是以交互方式使用 shell，但是也可以将希望执行的 JavaScript 文件传给 shell。直接在命令行中传递脚本就
        可以了:
            $ mongo script1.js script2.js script3.js
        mongo shell 会依次执行传入的脚本，然后退出。

        如果希望使用指定的主机/端口上的 mongod 运行脚本，需要先指定地址，然后在跟上脚本文件的名称
            $ mongo --quiet server -l:30000/foo script1.js script2.js script3.js

    2.7.3 创建 .mongorc.js 文件
        如果某些脚本会被频繁加载，可以将它们添加到 mongorc.js 文件中。这个文件会在启动 shell 时自动运行。

    2.7.4 定制shell提示



"""