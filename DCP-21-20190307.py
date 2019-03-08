"""
This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


class ClassTimes:

    def __init__(self, times):
        self.start = times[0]
        self.end = times[1]

    def __repr__(self):
        return str((self.start, self.end))

    def overlapping(self, ct):
        return (self.start > ct.start and self.start < ct.end) or (self.end > ct.start and self.end < ct.end)


def solve(times):
    return max([sum(1 for other_class in times if current_class.overlapping(other_class)) for current_class in times])


times = list(map(ClassTimes, [(30, 75), (0, 50), (60, 150), (40, 200), (80, 100), (210, 220), (0, 30), (0, 50)]))
print(sorted(times, key=lambda ct: ct.start))
rooms_needed = solve(times)
print(rooms_needed)
