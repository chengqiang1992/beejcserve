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

t = Data_test(2016, 8, 1)
t.out_data()
