"""
第三章 创建、更新和删除文档
    本章会介绍对数据库移入/移出数据的基本操作，具体包含如下操作：
        - 向集合添加新文档；
        - 从集合删除新文档；
        - 更新现有文档；
        - 为这些操作选择合适的安全级别和速度。

    3.1 插入并保存文档
        插入是向 MongoDB 中添加数据的基本方法。可以使用 insert 方法向目标集合插入一个文档:
            > db.foo.insert({"bar" : "baz"})
        这个操作会给文档自动增加一个 "_id"键（要是原来没有的话），然后将其保存到 MongoDB 中。

        3.1.1 批量插入
            如果要向集合中插入多个文档，使用批量插入会快一些。使用批量插入，可以将一组文档传递给数据库。

            在shell中，可以使用 batchInsert 函数实现批量插入，它与 insert 函数非常像，只是它接受的是一个文档数组作为参数

        3.1.2 插入校验

        写在最后
            insert(doc_or_docs, manipulate=True, check_keys=True, continue_on_error=False, **kwargs)
                Insert a document(s) into this collection.
                DEPRECATED - Use insert_one() or insert_many() instead.
                Changed in version 3.0: Removed the safe parameter. Pass w=0 for unacknowledged write operations.

        最新版本
            insert_one(document, bypass_document_validation=False)
            insert_many(documents, ordered=True, bypass_document_validation=False)

    3.2 Remove Data with PyMongo



"""

from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)
db = client.test

for x in range(1000000):
    db.tester.insert({})
    print("We're on time %d" % (x))



