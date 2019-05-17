# synchronized queue
import queue
import threading
import time
import random


def producer(tid):
    product_count = 0

    while product_count < max_num_of_products_for_each_producer:
        random_pick = random.randint(0, len(goods)-1)

        my_item = goods[random_pick] + '-' + str(product_count).rjust(3, '0')
        print("[%s] I am producing: %s" % (tid, my_item))
        q.put(my_item)

        product_count += 1

        time.sleep(1)

    print("[%s] Work done." % tid)
    q.task_done()


def consumer(tid):

    # waiting for initial products from producers
    time.sleep(3)

    while not q.empty():

        my_item = q.get()

        if my_item is None:
            print("[%s] Umm... nothing to eat. -_-;;" % tid)
        else:
            print("[%s] I am eating: %s" % (tid, my_item))
            q.task_done()

        time.sleep(2)

    print("[%s] Finish meal." % tid)


num_of_producers = 5
num_of_consumers = num_of_producers * 3

max_num_of_products_for_each_producer = 10

q = queue.Queue(10)
threads = []

goods = ['apple', 'orange', 'banana', 'grape', 'kiwi', 'mango'
         'grapefruit', 'tomato', 'carrot', 'lemon', 'tangerine', 'hanrabong', 'pineapple']

producer_name_prefix = 'PRODUCER-'
producer_count = 0

started_at = time.monotonic()

for i in range(num_of_producers):
    producer_count += 1
    t = threading.Thread(target=producer, args=(producer_name_prefix+str(producer_count).rjust(2, '0') + ': ',))
    t.start()
    threads.append(t)

consumer_name_prefix = 'CONSUMER-'
consumer_count = 0

for i in range(num_of_consumers):
    consumer_count += 1
    t = threading.Thread(target=consumer, args=(consumer_name_prefix+str(consumer_count).rjust(2, '0') + ': ',))
    t.start()
    threads.append(t)

# block until all tasks are done
q.join()

# stop workers
for i in range(num_of_producers + num_of_consumers):
    q.put(None)

for t in threads:
    t.join()

time_cost = time.monotonic() - started_at
print(f"Total cost time: {time_cost:.2f} second(s)")
