import os
import psutil

x = 7
process = psutil.Process(os.getpid())
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
print(process.memory_info().rss)  # in bytes 