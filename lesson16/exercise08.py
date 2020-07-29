class Time:
    def __init__(self, hour, minute, second):
        self.hour = self.__validate(hour,0,23)
        self.minute = self.__validate(minute,0,59)
        self.second = self.__validate(second,0,59)

    def set_hour(self, hour):
        self.hour = self.__validate(hour,0,23)

    def set_minute(self, minute):
        self.minute = self.__validate(minute,0,59)

    def set_second(self, second):
        self.second = self.__validate(second,0,59)

    def __validate(self, val, low, upp):
        if low <= val <= upp:
            return val
        else:
            return 0

    def total_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def print(self):
        print(f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}")

    def next_second(self):
        second = self.second + 1
        carry = second // 60
        second = second % 60

        minute = self.minute + carry
        carry = minute // 60
        minute = minute % 60

        hour = (self.hour + carry) % 24

        return Time(hour, minute, second)


t = Time(1,45,110)
t.print()

t1 = Time(11,12,13)
t1.next_second().print()

t1 = Time(11,12,59)
t1.next_second().print()

t1 = Time(11,59,59)
t1.next_second().print()

t1 = Time(23,59,59)
t1.next_second().print()