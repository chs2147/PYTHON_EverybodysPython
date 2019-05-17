# synchronized queue
import queue
import threading
import time


def worker(tid):
    while True:
        my_item = q.get()

        if my_item is None:
            break

        print(tid + "I am getting: " + my_item)
        my_item = '[%s]%s' % (tid, my_item)
        q.put(my_item)

        q.task_done()
        time.sleep(1)


num_of_workers = 3
q = queue.Queue()
threads = []
goods = ['apple', 'orange', 'banana', 'grape', 'kiwi', 'mango'
         'grapefruit', 'tomato', 'carrot', 'lemon', 'tangerine', 'hanrabong', 'pineapple']

thread_name_prefix = 'WORKER-'
thread_count = 0

for i in range(num_of_workers):
    thread_count += 1
    t = threading.Thread(target=worker, args=(thread_name_prefix+str(thread_count).rjust(2, '0') + ': ',))
    t.start()
    threads.append(t)

# put data in queue
for fruit in goods:
    q.put(fruit)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_of_workers):
    q.put(None)

for t in threads:
    t.join()
