# synchronized queue
import queue
import threading
import time
import random
import sys


def producer(tid):
    product_count = 0

    while product_count < max_num_of_products_for_each_producer:
        random_pick = random.randint(0, len(goods)-1)

        my_item = goods[random_pick] + '-' + str(product_count).rjust(3, '0')
        print("%s[%s] I am producing: %s" % (producer_indent, tid, my_item))
        product_queue.put(my_item)

        product_count += 1

        time.sleep(.500)

    print("%s[%s] Work done." % (producer_indent, tid))

    product_queue.task_done()


def consumer(tid):

    # waiting for initial products filled from producers
    time.sleep(1)

    # init count of eat
    eat_count = 0

    while not product_queue.empty():

        my_item = product_queue.get()

        if my_item is None:
            print("%s[%s] Umm... nothing to eat. -_-;;" % (consumer_indent, tid))
        else:
            print("%s[%s] I am eating: %s" % (consumer_indent, tid, my_item))
            eat_count += 1

            product_queue.task_done()

        time.sleep(2)

    print("%s[%s] Finish meal." % (consumer_indent, tid))
    consumer_stat_dict[tid] = eat_count


if not __name__ == '__main__':
    sys.exit()

# define number of threads for each role
num_of_producers = 5
num_of_consumers = num_of_producers * 3

# define the minimum number of items that each consumer can eat
min_num_of_items_for_each_consumer = 10

# define the maximum limits of resource for exiting threads
max_num_of_products_for_each_producer = (num_of_consumers * min_num_of_items_for_each_consumer) \
                                        / num_of_producers

# create product queue
product_queue = queue.Queue(num_of_consumers * 2)

# thread list
threads = []

goods = ['apple', 'orange', 'banana', 'grape', 'kiwi', 'mango'
         'grapefruit', 'tomato', 'carrot', 'lemon', 'tangerine', 'hanrabong', 'pineapple']

# start counting time-cost
started_at = time.monotonic()

# start producer threads
producer_name_prefix = 'PRODUCER-'
producer_count = 0
producer_indent = '-' * 4

for i in range(num_of_producers):
    producer_count += 1
    t = threading.Thread(target=producer, args=(producer_name_prefix+str(producer_count).rjust(2, '0'),))
    t.start()
    threads.append(t)

# start consumer threads
consumer_name_prefix = 'CONSUMER-'
consumer_count = 0
consumer_indent = '*' * 2
consumer_stat_dict = {}

for i in range(num_of_consumers):
    consumer_count += 1
    new_id = consumer_name_prefix+str(consumer_count).rjust(2, '0')
    consumer_stat_dict.setdefault(new_id, 0)
    t = threading.Thread(target=consumer, args=(new_id,))
    t.start()
    threads.append(t)

# block until all tasks are done
product_queue.join()

# stop workers
for i in range(num_of_producers + num_of_consumers):
    product_queue.put(None)

for t in threads:
    t.join()

# start summary section
print()
print('-' * 80)

# calculate total time-cost for processing
time_cost = time.monotonic() - started_at
print(f"Total cost time: {time_cost:.2f} second(s)")

# statistics of eat count for each consumer
print()
print('-- Statistics of consume count for each consumer --')
for k, v in consumer_stat_dict.items():
    print("   * {0} {1}".format(str(k).ljust(20, '.'), str(v).rjust(3)))

# end summary section
print('-' * 80)
