"""
3.3 更新文档
    文档存入数据库以后，就可以使用update方法来更新它。update两个参数，一个是查询文档，用于定位需要更新的目标文档；另一个
    是修改器(modifier)文档，用于说明要对找到的文档进行哪些修改。

    更新操作是不可分割的：若是两个更新同时发生，先到达服务器的先执行，接着执行另外一个。所以，两个需要同时进行的更新会迅
    速接连完成，此过程不会破坏文档：最新的更新会取得“胜利”。

    3.3.1 文档替换
        最简单的更新就是一个新文档完全替换匹配的文档。这是用于进行大规模模式迁移的情况。例如，要对下面的用户文档做一个
        比较大的调整。
            {
                "_id": ObjectID("4b2b9f67a1f631733d917a7a"),
                "name": "joe",
                "friends": 32,
                "enemies": 2
            }
        我们希望将 "friends"  和 "enemies" 两个字段移到 "relationships" 子文档中。我们可以在shell中改变文档结构，然后使用
        update 替换数据库中的当前文档：
            var joe = db.users.findOne({"name": "joe"})
            joe.relationships = {"friends": joe.friends, "enemies": joe.enemies}
            joe.username = joe.name
            delete joe.friends
            delete joe.enemies
            delete joe.name
            db.users.update({"name": "joe"}, joe)
        现在用 findOne查看更新后的文档结构。

        一个常见的错误就是查询条件匹配到了多个文档，然后更新时由于第二个参数存在就长生了重复的"_id"值。数据库会抛出错误，
        任何文档都不会更新。

        例如，有好几个文档都有相同的 "name" 值，但是我们没有意识到：
            > db.people.find()
            {"name": "joe", "age": 65},
            {"name": "joe", "age": 20},
            {"name": "joe", "age": 49},
        现在如果第二个Joe过生日，要增加"age"的值，我们可能会这么做：
            > joe = db.people.fineOne({"name": "joe", "age": 20})
            joe.age++
            db.people.update({"name": "joe"}, joe)      执行出错了
        到底是怎么了？ 调用update时，数据库会查找一个"name"值为"joe"的文档。找到的第一个65岁的Joe。然后数据库试着用变量
        joe中的内容替换找到的文档，但是会发现集合里面已经有一个具有同样"_id"的文档。所以，更新就会失败，因此"_id"值必须唯
        一。为了避免这种情况，最好确保更新时总是指定一个唯一文档，例如使用"_id"这样的键来匹配。对于上面的例子，这才是正
        确的更新方法：
            > db.people.update({"_id": ObjectId("589c4af5e1f02894a27feb32")}, joe)

    3.3.2 使用修改器
        通常文档只会有一部分要更新。可以使用原子性的更新修改器(update modifier)，指定对文档中的某些字段进行更新。更新修改
        器是中特殊的键，用来制定复杂的更新操作，比如修改、增加或者删除键，还可能是操作数组或者内嵌文档。

        假设要在一个集合中放置网站的分析数据，只要有人访问页面，就增加计数器。可以使用更新修改原子性地完成这个增加。每个
        URL及对应的访问呢次数都以如下方式存储在文档中：
            {
                "_id": ObjectId("4b253b067525f35f94b60a31"),
                "url": "www.baidu.com",
                "pageviews": 52
            }
        每次有人访问页面，就通过URL找到该页面，并用 "$inc" 修改器增加 "pageviews" 的值。
            > db.analytics.update({"url": "www.baidu.com"}, {"$inc": {"pageviews": 1}})
        现在，执行一个 find 操作，会发现 "pageviews" 的值增加了1。
            > db.analytics.find()
        使用修改器时，"_id" 的值不能改变。（注意，整个文档替换时可以改变"_id"。）其他键值，包括其他唯一索引的键，都是可
        以改变的。

        1. "$set" 修改器入门
        "$set" 用来指定一个字段的值。如果这个地段不存在，则创建它。这对更新模式或者增加用户定义的键来说非常方便。例如，
        用户资料存储在下面这样的文档中：
            > db.users.findOne()
            > db.users.insert({"_id": ObjectId("4b253b067525f35f94b60a31"), "name": "joe", "age": 30, "sex": "male", "location": "Wisconsin"})
        非常简要的一段用户信息。要想添加喜欢的数据进去，可以使用 "$set"：
            > db.users.update({"_id": ObjectId("4b253b067525f35f94b60a31")}, {"$set": {"favorite book": "War and Peace"}})
        之后就有了 "favorite book"键。
            > db.users.findOne()
            {
                "_id" : ObjectId("4b253b067525f35f94b60a31"),
                "name" : "joe",
                "age" : 30.0,
                "sex" : "male",
                "location" : "Wisc

                onsin",
                "favorite book" : "War and Peace"
            }
        要是用户觉得喜欢的其实是另外一本书， "$set"又能帮上忙了：
            > db.users.update({"_id": ObjectId("4b253b067525f35f94b60a31")}, {"$set": {"favorite book": "Green Eggs and Ham"}})
        用"$set"设置可以修改键的类型。例如，如果用户觉得喜欢很多本书，就可以将 "favorite book"键的值变成一个数组：
            > db.users.update({"_id": ObjectId("4b253b067525f35f94b60a31")}, {"$set": {"favorite book": ["Cat's Cradle", "Foundation Trilogy", "Ender;s Game"]}})
        如果用户突然发现自己其实不爱读书，可以用 "$unset" 将这个键完全删除：
            > db.uses.update({"name": joe}, {"$unset": {"favorite book": 1}})

        也可以使用"$set"修改内嵌文档

        2. 增加和减少
            "$inc" 修改器用来增加已有的键，或者该键不存在那就创建一个。对于更新分析数据、因果关系、投票或者其他有变化数值的地方，使用这个都会非常方便。

            假如建立一个游戏集合，将游戏和变化的分数都存储在里面。比如用户玩弹球(pinball)游戏，可以插入一个包含游戏名和玩家的文档来标识不同的游戏：
                > db.games.insert({"game": "pinball", "user": "joe"})
            要是小球撞到了砖块，就会给玩家加分。分数可以随便给，这里就把玩家得分技术约定成50好了。使用 "$inc" 修改器给玩家加50分：
                > db.games.update({"game": "pinball", "user": "joe"}, {"$inc": {"score": 50}})
            更新后，可以看到:
                > db.games.findOne()
                {
                    "_id" : ObjectId("589c634ee1f02894a27feb34"),
                    "game" : "pinball",
                    "user" : "joe",
                    "score" : 50.0
                }
            分数原来并不存在，所以 "$inc" 创建了这个键，并把值设定成增加量: 50。

            如果小球落入加分去，要加 10 000分。只要给 "$inc" 传递一个不同的值就好了：
                > db.games.update({"game": "pinball", "user": "joe"}, {"$inc": {"score": 10000}})
            "$inc"与"$set"的和用法类似，就是专门来增加（和减少）数字的。"$inc"只能用于整形、长整形或双精度浮点型的之。
            另外，"$inc" 键的值必须为数字。

        3. 数组修改器
            有一大类很重要的修改器可用于修改数组。数组是常用且非常有用的数据结构：它们不仅是可通过索引进行引用的列表，而且还可以作为数据集(set)来用。

        4. 添加元素
            如果数组已存在， "$push" 会向已有的数组末尾加入一个元素，要是没有就创建一个新的数组。
                > db.blog.posts.insert({"_id": ObjectId("4b2d75476cc613d5ee930164"), "title": "A blog post", "content": "..."})
                > db.blog.post.findOne()
                    {
                        "_id" : ObjectId("4b2d75476cc613d5ee930164"),
                        "title" : "A blog post",
                        "content" : "..."
                    }
            可以想还不存在的"comments"数组添加一条评论，这个数组会被dion个创建，并加入一条评论：
                > db.blog.posts.update({"title": "A blog post"}, {"$push": {"comments": {"name": "bob", "email": "bob@example.com", "content": "good.post."}}})
            要是还想添加一条评论，继续使用 "$push"
                使用 "$each"子操作符，可以通过一次 "$push"操作添加多个值，
                使用如果希望数组的最大长度是固定，那么可以将 "$slice" 和 "$push" 组合在一起使用，这样就可以保证数组不会超过设定好的最大的长度，这机上就得到了一个最多包含N个元素的数组：
                可以在清理元素之前使用"$sort"，只要向数组中添加子对象就需要清理
        5. 将数组作为数据集使用
            > db.papers.update({"authors cited": {"$ne": "Richie"}}, {$push: {"author sited": Richie}})

            添加新地址时，用"$addToSet"可以避免插入重复地址：
                > db.users.update({"_id": ObjectId("4b2d75476cc613d5ee930164")}, {"$addToSet": {"emails": "joe@gmail.com"}})

            将"$addToSet"和"$each"组合起来，可以添加多个不同的值，而用"$ne"和"$addToSet"

        6. 删除元素
            有几个从数组中删除元素的方法，若是把数组看成队列或者栈，可以用 "$pop"， 这个修改器可以从数组任何一段删除元素。
                > db.blog.posts.insert({"_id": ObjectId("4b2d75476cc613d5ee930164"), "title": "A blog post", "content": "..."})
                > db.blog.posts.findObe()

        7. 基于位置的数组修改器
            若是数组有多个值，而我们只想对其中的一部分进行操作，就需要一些技巧。有两种方法操作数组中的值：通过位置或者定位操作符("$")

        8. 修改器速度


    3.3.3 upsert
        upsert是一种特殊的更新。要是没有找个符合更新条件的文档，就会以这个条件和更新文档为基础创建一个新的文档。如果找到了匹配的文档，则正常更新。
        upsert非常方便，不必预置集合，同一套代码既可以用于创建文档又可以用于更新文档。

        我们回过头来看看那个记录网站页面访问次数的例子。要是没有upsert、就得试着查询URL，没有找到就得新建一个文档，找到的话就增加访问次数。要是把
        这个写成 JavaScript 程序，会是下面这样的：
            // 检查这个页面是否有一个文档
            blog = db.analytics.findOne({"url": "/blog"})

            // 如果有，就将视图数加1并保存
            if (blog) {
                blog.pageviews++;
                db.analytics.save(blog);
            }
            // 否则为这个页面创建一个新文档
            else {
                db.analytics.save({"url": "/blog", "pageviews": 1})
            }
        这就是说如果有人访问那页面，我们得先对数据库进行查询，然后选择更新或插入。要是多个进程同时运行这段代码，还会遇到同时对给定URL插入多个文档这样的竞态条件。

        要是使用 upsert，既可以避免竞态问题，又可以缩减代码量 (update 的第三个参数表示这是个upsert):
            > db.analytics.update({"url": "/blog"}, {"$inc": {"pageviews": 1}}, true)
        这行代码和之前的代码作用完全一样，但他更高效，并且是原子性的！ 创建新文档会将条件文档作为基础，然后对它应用修改器文档。


    3.4 写入安全机制
        写入安全(Write Concern)是一个客户端设置，用于控制写入的安全级别。默认情况下，插入、删除和更新都会一直等待数据库
        响应(写入是否成功)，然后才会继续执行。通常，遇到错误时，客户端会抛出一个异常(有些语言中可能不叫"异常"，不过实质
        上都是类似的东西)。

        有一些选项可以用于精确控制需要应用程序等待的内容。两种最基本的写入安全机制是应答式写入(acknowledged write) 和非
        应答式写入(unacknowledged write)。应答式写入是默认的方式：数据库会给出响应，告诉你写入操作是否成功执行。非应答式
        写入不返回任何响应，所以无法知道写入是否成功。

        通常来说，应用程序应该使用应答式。但是，对于一些不是特别重要的数据（比如日志或者批量加载数据），你可能不愿意为了
        自己不关心的数据而等待数据库响应。在这种情况下，可以使用非应答式写入。

        尽管非应答式写入不返回数据错误，但是这不代表应用程序不需要做错误检查。如果尝试向已关闭的套接字(socket)执行写入，
        或者写入套接字时发生了错误，都会引起异常。

        使用非应答式写入时，一种经常被忽视的错误是插入无效数据。比如，如果试图插入两个具有相同"_id"字段的文档，shell就会
        抛出异常：
            > db.foo.insert({"_id": 1})
            > db.foo.insert({"_id": 1})
            E11000 duplicate key error index: test.foo.$_id dup key: {: 1.0}

        如果第二次插入时使用非应答式写入，那么第二次插入就不会抛出异常。键重复异常是一种非常常见的错误，还有其他类似的错
        误，比如无效的修改器或者是磁盘空间不足。

        事实上，还有其他一些写入安全机制，第11章会讲诉多台服务器之间的写入安全，第19章会讲诉写入提交。

        2012年，默认的写入安全机制改变了，所以，遗留代码的行为可能会与预期不一致。在此之前，默认的写入是非应答式。

        幸好，很容易得知当前代码是在默认的写入安全机制发生变化之前写的还是之后写的：默认的写入机制变为安全写入以后，所有
        驱动程序开始使用MongoClient这个类。如果程序使用的对象是Mongo或者Connection或者其他内容，那么这段程序使用的就是旧
        的、默认不安全的API。在默认写入安全机制发生变化之前，任何语言都没有使用MongoClient作为类型，所以，如果你的代码使
        用了这个类，说明你的代码是写入安全的。

        如果使用的连接不是MongoClient，应在必要时将旧代码中的非应答式写入改成应答式写入。

"""


