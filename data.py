
class Calender:

    def __init__(self):
        self.data = {
            "Jan": 1,
            "Feb": 2,
            "Mar": 3,
            "Apr": 4,
            "May": 5,
            "Jun": 6,
            "Jul": 7,
            "Aug": 8,
            "Sep": 9,
            "Oct": 10,
            "Nov": 11,
            "Dec": 12
        }
        self.reversed_data = {y: x for (x, y) in self.data.items()}
    
    def NametoNum(self, name):

        return self.data.get(name)

    def NumtoName(self, num):

        return self.reversed_data.get(num)
