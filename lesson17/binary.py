class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:" \
               f"{str(self.minute).zfill(2)}:" \
               f"{str(self.second).zfill(2)}"

    def __gt__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True
            elif self.minute == other.minute:
                if self.second > other.second:
                    return True
        return False

    def __ge__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            if self.minute > other.minute:
                return True
            elif self.minute == other.minute:
                if self.second >= other.second:
                    return True
        return False

    def __eq__(self, other):
        if isinstance(other, Time):
            if self.hour == other.hour and self.minute == other.minute and self.second == other.second:
                return True
            return False
        elif isinstance(other, int):
            print(Time(other,0,0))
            return self == Time(other, 0, 0)

    def __add__(self, other):
        if isinstance(other, Time):
            carry = (self.second + other.second) // 60
            new_second = (self.second + other.second) % 60
            carry = (self.minute + other.minute + carry) // 60
            new_minute = (self.minute + other.minute + carry) % 60
            new_hour = (self.hour + other.hour + carry) % 24
            return Time(new_hour, new_minute, new_second)
        elif isinstance(other, int):
            return Time((self.hour + other)%24, self.minute, self.second)

    def __radd__(self, other):
        return self.__add__(other)


print(Time(7,44,55) + Time(10,22,5))
print(Time(7,44,55) + 19)
print(19 + Time(7,44,55))

