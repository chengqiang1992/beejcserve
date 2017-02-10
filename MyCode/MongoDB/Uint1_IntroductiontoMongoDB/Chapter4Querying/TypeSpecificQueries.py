"""
第四章 查询
    本章将详细介绍查询。主要会涵盖一下几个方南：
        - 使用find或者findOne函数和查询文档对数据库执行查询；
        - 使用$条件查询实现范围查询、数据集合包含查询、不等式查询，以及其他一些查询；
        - 查询会返回一个数据库游标，游标只会在你需要时才将需要的文档批量返回；
        - 还有很多针对游标执行的员操作，包括忽略一定数量的结果，或者限定返回结果的数量，以及对结果的排序。

    4.3 特定类型的查询
        如第二章所述，MongoDB 的文档可以使用多种类型的数据。其中有一些在查询时会有特别的表现。
        4.3.1 null
            null类型的行为有点奇怪。它确实能匹配自身，所以要是有一个包含如下文档的集合：
                > db.c.find()
                {"_id": ObjectId("4ba0f0dfd22aa494fd523621"), "y": null}
                {"_id": ObjectId("4ba0f0dfd22aa494fd523622"), "y": 1}
                {"_id": ObjectId("4ba0f0dfd22aa494fd523623"), "y": 2}
            就可以按照预期的方式查询"y"键为null的文档：
                > db.c.find({"y": null})
                {"_id": ObjectId("4ba0f0dfd22aa494fd523621"), "y": null}
            但是，null不仅会匹配某个键的值为null的文档，而且还会匹配不包含这个键的文档。所以，这种匹配还会返回缺少这个键
            的所有文档：
                > db.c.find({"z": null})
                {"_id": ObjectId("4ba0f0dfd22aa494fd523621"), "y": null}
                {"_id": ObjectId("4ba0f0dfd22aa494fd523622"), "y": 1}
                {"_id": ObjectId("4ba0f0dfd22aa494fd523623"), "y": 2}
            如果仅想匹配键值为null的文档，既要检查该键的值是否为null，还要通过"$exists"条件判定键值已存在：
                > db.c.find({"z": {"$in": [null], "$exists": true}})
            很遗憾，没有"$eq"操作符，所以这条查询语句看上去令人费解，但是使用只有一个元素的"$in"操作符效果是一样的。
        4.3.2 正则表达式
            正则表达式能够灵活有效地匹配字符串。例如，想要查找所有名为Joe或者joe的用户，就可以使用正则表达式执行不区分大
            小写的匹配：
                > db.users.find({"name": /joe/i})
            系统可以接受正则表达式标志(i)，但不是一定要有。现在已经匹配了各种大小写组合形式的joe，如果还希望匹配如"joey"
            这样的键，可以略微修改一下刚刚的正则表达式：
                > db.users.find({"name": /joe?/i})
            MongoDB 使用 Perl兼容的正则表达式(PCRE)库来匹配正则表达式，任何PCRE支持的正则表达式语法都能被MongoDB接受。建
            议在查询中使用正则表达式前，现在JavaScript shell中检查一下语法，确保匹配与设想的一致。
        4.3.2 查询数组
            查询数组与查询标量值是一样的。例如，有一个水果列表，如下所示：
                > db.food.insert({"fruit": ["apple", "banana", "peach"]})
            下面的查询：
                > db.food.find({"fruit": "banana"})
            会成功匹配该文档。这个查询好比我们对一个这样的（不合法）文档进行查询：
                {"fruit": "apple", "fruit": "banana", "fruit": "peach"}.
            1. $all
                如果需要通过多个元素来匹配数组，就要用"$all"了。这样就会匹配一组元素。
                例如，假设创建了一个包含3个元素的集合：
                    > db.food.insert({"_id": 1, "fruit": ["apple", "banana", "peach"]})
                    > db.food.insert({"_id": 2, "fruit": ["apple", "kumquat", "orange"]})
                    > db.food.insert({"_id": 3, "fruit": ["cherry", "banana", "apple"]})
                要找到既有"apple"又有"banana"的文档，可以使用 "$all"来查询：
                    > db.food.find({"fruit": {$all: ["apple", "banana"]}})

                要是想要查询数组特定位置的元素，需使用key.index语法指定瞎掰哦：
                    > db.food.find({"fruit.2": "peach"})
            2. $size
                "$size"对于查询数组来说也非常有用的，顾名思义，可以用它来查询特定长度的数组。例如：
                    > db.food.find({"fruit": {"$size": 3}})

            3. $slice操作符
                本章前面已经提及，find的第二个参数是可选的，可以指定需要返回的键。这个特别的"$slice"操作符可以返回某个键
                匹配的数组元素的一个子集。

                例如，假设现在有一个博客文章的文档，我们希望返回前10条评论，可以这样做：
                    > db.blog.posts.findOne(criteria, {"comments": {"$slice": 10}})
                也可以返回后10条评论
                    > db.blog.posts.findOne(criteria, {"comments": {"$slice": -10}})
                "$slice"也可以指定偏移值以及希望返回的元素数量，来返回元素集合中间位置的某些结果
                    > db.blog.posts.findOne(criteria, {"comments": {"$slice": [23, 10]}})
                这个操作会跳过前23个元素，返回第24-33个元素，如果数组不够33个元素，则返回第23个元素后面的所有元素。
            4. 返回一个匹配的数组元素

            5. 数组和范围查询的相互作用
        4.3.4 查询内嵌文档
            点表示法也是待插入前或者提取后执行一个全局替换。

    4.4 $where查询
        键/值对是一种表达能力非常好的查询方式，但是依然有些需求它无法表达。其他方法都败下阵时，就轮到"$where"子句登场了，
        用它可以在查询中执行任意的JavaScript。这样就能在查询中做（几乎）任何事情。为了安全期间，应该严格限制或者消除"$where"
        语句的使用。应该禁止终端用户使用任意的"$where"语句。

        "$where"语句最常见的应该就是比较文档中的两个键的值是否相等。假如我们有如下文档：
            > db.foo.insert({"apple": 1, "banana": 6, "peach": 3})
            > db.foo.insert({"apple": 8, "spinach": 4, "watermelon": 4})
        我们希望返回两个键具有相同值的文档。第二个文档中，"spinach"和"watermelon"的值相同，所以需要返回该文档。MongoDB似
        乎从来没有提供过一个$条件语句来做这种查询，所以只能用"$where"子句借助JavaScript来完成了：
            > db.foo.find({"$where": function() {
                for(var current in this){
                    for(var other in this){
                        if(current != other && this[current] == this[other]){
                            return true;
                        }
                    }
                }
                return false
            }})
        不是非常必要时，一定要避免使用"$where"查询，因为他们在速度上要比常规查询慢很多。每个文档都要从BSON转成成JavaScript
        对象，然后通过"$where"表达式来运行。而且"$where"语句不能使用索引。

        服务器端脚本
            在服务器上执行JavaScript时必须注意安全性。如果使用不当，服务器端JavaScript很容易受到注入攻击，与关系型数据库
            中的注入攻击很类似。
"""