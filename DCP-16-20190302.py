"""
This problem was asked by Twitter.
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:
record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
"""

class Log:

    def __init__(self, records=list()):
        self.records = records

    def record(self, order_id):
        self.records.append(order_id)

    def get_last(self, i=0):
        # i=0 is the very last elemnt
        record = self.records[-(i + 1)] if i != 0 else self.records[-1]
        print(record)
        return record


log = Log()
for i in range(1000):
    log.record(i)

log.get_last()
log.get_last(1)
log.get_last(-2)
