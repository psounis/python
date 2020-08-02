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
        if self.hour == other.hour and self.minute == other.minute and self.second == other.second:
            return True
        return False


t = Time(11,1,2)
t2 = Time(11,1,1)
print(f"{t} > {t2}: {t>t2}")
print(f"{t} < {t2}: {t<t2}")
print(f"{t} >= {t2}: {t>=t2}")
print(f"{t} <= {t2}: {t<=t2}")
print(f"{t} == {t2}: {t==t2}")
print(f"{t} != {t2}: {t!=t2}")
