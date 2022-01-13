"""
Memcache
System
Medium
Accepted Rate
46%

DescriptionSolutionNotesDiscussLeaderboard
Description
Implement a memcache which support the following features:

get(curtTime, key) Get the key's value, return 2147483647 if key does not exist.
set(curtTime, key, value, ttl) Set the key-value pair in memcache with a time to live (ttl). The key will be valid from curtTime to curtTime + ttl - 1 and it will be expired after ttl seconds. if ttl is 0, the key lives forever until out of memory.
delete(curtTime, key) Delete the key.
incr(curtTime, key, delta) Increase the key's value by delta return the new value. Return 2147483647 if key does not exist.
decr(curtTime, key, delta) Decrease the key's value by delta return the new value. Return 2147483647 if key does not exist.
It's guaranteed that the input is given with increasing curtTime.

Actually, a real memcache server will evict keys if memory is not sufficient, and it also supports variety of value types like string and integer. In our case, let's make it simple, we can assume that we have enough memory and all of the values are integers.

Search "LRU" & "LFU" on google to get more information about how memcache evict data.

Try the following problem to learn LRU Cache

Example
Example1

get(1, 0)
>> 2147483647
set(2, 1, 1, 2)
get(3, 1)
>> 1
get(4, 1)
>> 2147483647
incr(5, 1, 1)
>> 2147483647
set(6, 1, 3, 0)
incr(7, 1, 1)
>> 4
decr(8, 1, 1)
>> 3
get(9, 1)
>> 3
delete(10, 1)
get(11, 1)
>> 2147483647
incr(12, 1, 1)
>> 2147483647

"""


class MemNode:
    def __init__(self, value, expiredtime):
        self.value = value
        self.expiredtime = expiredtime

    def live_forever(self):
        self.expiredtime = float("inf")


class Memcache:
    def __init__(self):
        # do intialization if necessary
        self.memory = {}
        self.not_exist = 2147483647

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """

    def get(self, curtTime, key):
        # write your code here
        if self.remove_expired_cache(key, curtTime):
            return self.not_exist
        return self.memory[key].value

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """

    def set(self, curtTime, key, value, ttl):
        # write your code here
        memnode = MemNode(value, curtTime + ttl - 1)
        if ttl == 0:
            memnode.live_forever()
        self.memory[key] = memnode

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """

    def delete(self, curtTime, key):
        # write your code here
        if key in self.memory:
            del self.memory[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def incr(self, curtTime, key, delta):
        # write your code here
        if self.remove_expired_cache(key, curtTime):
            return self.not_exist
        self.memory[key].value += delta
        return self.memory[key].value

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """

    def decr(self, curtTime, key, delta):
        # write your code here
        if self.remove_expired_cache(key, curtTime):
            return self.not_exist
        self.memory[key].value -= delta
        return self.memory[key].value

    def remove_expired_cache(self, key, curtTime):
        """
        :param key:
        :param curtTime:
        :return:
        This need to be an another cron job based service which will run every second to delete cache
        """
        if key not in self.memory:
            return True
        if self.memory[key].expiredtime < curtTime:
            self.delete(curtTime, key)
            return True
        return False
