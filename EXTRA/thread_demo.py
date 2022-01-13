import threading

counter = 0
def counter_inc():
    global counter
    counter += 1

def test(lock):
    
    for _ in range(1000000):
        with lock:
            counter_inc()
        
    # print(counter)

def main():
    global counter
    counter = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=test, args=(lock,))
    t2 = threading.Thread(target=test, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    for i in range(10):
        main()
        print(f"{i} --> {counter}")

    
