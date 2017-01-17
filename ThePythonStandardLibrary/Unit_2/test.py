class Data_test(object):
    day = 0
    month = 0
    year = 0

    def __init__(self, year=0, month=0, day=0):
        self.day = day
        self.month = month
        self.year = year

    def out_data(self):
        print("year:" + self.year + " month:" + self.month + " day:" + self.day)

t = Data_test('2016', '8', '1')
t.out_data()


# class Data_tets2(object):
#     day = 0
#     month = 0
#     year = 0
#
#     def __init__(self, year=0, month=0, day=0):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def out_date(self):
#         print("year:" + self.year + " month:" + self.month + " day:" + self.day)
#
#     @classmethod
#     def get_date(cls, data_as_string):
#         # 这里的第一个参数是cls，表示调用当前的类名
#         year, month, day = map(int, data_as_string.split('-'))
#         datel = cls(year, month, day)
#         return datel
#
# r = Data_tets2.get_date("2016-8-6")
# r.out_date()

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'two': 2, 'one': 1})

print(a)
print(b)
print(c)
print(d)
print(e)
print(a == b == c == e)
