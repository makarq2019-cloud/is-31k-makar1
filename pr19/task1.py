import threading

def task(name):
    for i in range(1, 6):
        print(name, i)

t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()