import threading

ct1 = 0
ct2 = 0
ct3 = 0
ct4 = 0
ct5 = 0
ct6 = 0


class XThread(threading.Thread):
    ct = -1

    def __init__(self, max_thread, data):
        self.data = data
        self.max_thread = max_thread
        threading.Thread.__init__(self)


        XThread.ct += 1
        self.index = XThread.ct

    def count_ranges(self):
        global ct1, ct2, ct3, ct4, ct5, ct6
        for i in range(self.index, len(self.data), self.max_thread):
            if 20 <= self.data[i] < 30:
                ct1 += 1
            elif 30 <= self.data[i] < 40:
                ct2 += 1
            elif 40 <= self.data[i] < 60:
                ct3 += 1
            elif 60 <= self.data[i] < 70:
                ct4 += 1
            elif 70 <= self.data[i] < 100:
                ct5 += 1
            else:
                ct6 += 1

    def run(self):
        self.count_ranges()


threads = []
max_thread = int(input("Informe o número de threads: "))
data = [30, 39, 40, 41, 47, 70, 64, 29,
        100, 47, 22, 30, 79, 66, 69]

for i in range(0, max_thread):
    t = XThread(max_thread, data)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("20-30:", ct1)
print("30-40:", ct2)
print("40-60:", ct3)
print("60-70:", ct4)
print("70-100:", ct5)
print("> 100:", ct6)