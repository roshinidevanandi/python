import time
print(time)

# _______________MODULES___________

# 1.time()
# 2.ctime()
# 3.localtime()
# 4.strftime()
# 5.gmtime()
# 6.mktime()
# 7.asctime()


# time()
# print(time.time())
# print(time.time_ns())


# ctime() ->current time
# print(time.ctime())
# print(time.ctime(1744112657.1253412))


# localtime() ->It will also give the complete structure of the current time 
# print(time.localtime())
# print(time.localtime().tm_mon)
# print(time.localtime().tm_min)

# strftime() ->string from time
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# print(time.strftime("%A",time.localtime()))
# print(time.strftime("%a",time.localtime()))
# print(time.strftime("%B",time.localtime()))
# print(time.strftime("%y",time.localtime()))
# print(time.strftime("%b",time.localtime()))
# print(time.strftime("%M",time.localtime()))  ->minutes


# gmtime() ->Greenwich Mean Time --->This time is 5 hours different from indian's time
# print(time.gmtime()) 

# mktime() ->maketime
# print(time.mktime((2025,4,19,17,0,0,0,0,0)))


# asctime()  ->current time
# print(time.asctime()) 




