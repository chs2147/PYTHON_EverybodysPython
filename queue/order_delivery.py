# synchronized queue
import queue
import threading
import time
import random
import sys
from termcolor import colored


def producer(tid):
    product_count = 0

    while product_count < max_num_of_products_for_each_producer:

        random_pick = random.randint(0, len(goods)-1)

        my_item = goods[random_pick] + '-' + str(product_count).rjust(3, '0')
        print("%s[%s] I am producing: %s" % (producer_indent, tid, my_item))

        # enqueue new product to product queue
        product_queue.put(my_item)

        product_count += 1
        time.sleep(.100)

    print("%s[%s] Work done." % (producer_indent, tid))


def servant(tid):

    # waiting for initial products filled from producers
    time.sleep(1)

    # init inventory
    inventory = []

    while not (product_queue.empty() and len(inventory) == 0):

        # dequeue product from product queue
        my_item = product_queue.get()

        if my_item is None:
            print("%s[%s] Oops... nothing to store. -_-;;" % (servant_indent, tid))
        else:
            print(colored("%s[%s] Add product <%s> to inventory" % (servant_indent, tid, my_item), 'green'))

            # stores item on inventory
            inventory.append(my_item)

            # store count for statistic
            servant_stat_dict[tid] += 1

            product_queue.task_done()

        # dequeue order from order queue
        order = order_queue.get()

        if order is not None:
            amount = order['amount']
            items = order['products']

            print(colored("%s[%s] Get order from: %s" % (servant_indent, tid, order['thread_id']), 'blue'))

            for _ in range(amount):
                if len(inventory) > 0:
                    items.append(inventory.pop())

            print(colored("%s[%s] Fill pocket with: %s" % (servant_indent, tid, str(items)), 'blue'))

        order_queue.task_done()

        time.sleep(2)

    print("%s[%s] Inventory out of stocks." % (servant_indent, tid))


def consumer(tid):

    # waiting for initial products filled from producers
    time.sleep(2)

    # init pocket
    my_pocket = []

    # init order form
    order_form = {}
    order_form.setdefault('thread_id', tid)
    order_form.setdefault('amount', 1)
    order_form.setdefault('products', my_pocket)

    while True:

        print(colored("%s[%s] POCKET: %s" % (consumer_indent, tid, my_pocket), 'yellow'))

        if len(my_pocket) == 0:
            print("%s[%s] Pocket empty. Place new order to servant" % (consumer_indent, tid))
            order_queue.put(order_form)
        else:
            time.sleep(2)
            pick_item = my_pocket.pop()

            if pick_item is not None:
                consumer_stat_dict[tid] += 1
                print(colored("%s[%s] Consume product <%s> from my pocket" % (consumer_indent, tid, pick_item), 'red'))

        time.sleep(2)


# only run on main
if not __name__ == '__main__':
    sys.exit()

# define number of threads for each role
num_of_producers = 2
num_of_servants = num_of_producers * 2
num_of_consumers = num_of_servants * 3

# define minimum amount of products that consumer can consume
min_num_of_products_for_each_consumer = 4

# define the maximum limits of resource for exiting threads
max_num_of_products_for_each_producer = num_of_consumers * min_num_of_products_for_each_consumer / num_of_producers

# create product queue
product_queue = queue.Queue(num_of_servants * 2)

# create order queue
order_queue = queue.Queue(num_of_consumers)

# thread list
threads = []

goods = ['apple', 'orange', 'banana', 'grape', 'kiwi', 'mango'
         'grapefruit', 'tomato', 'carrot', 'lemon', 'tangerine', 'hanrabong', 'pineapple']

# start counting time-cost
started_at = time.monotonic()

# for statistic
servant_stat_dict = {}
consumer_stat_dict = {}

try:

    # start producer threads
    producer_name_prefix = 'PRODUCER-'
    producer_count = 0
    producer_indent = '-' * 6

    for i in range(num_of_producers):
        producer_count += 1
        t = threading.Thread(target=producer, args=(producer_name_prefix+str(producer_count).rjust(2, '0'),))
        t.start()
        threads.append(t)

    # start servant threads
    servant_name_prefix = 'SERVANT-'
    servant_count = 0
    servant_indent = '*' * 4

    for i in range(num_of_servants):
        servant_count += 1
        new_id = servant_name_prefix + str(servant_count).rjust(2, '0')
        servant_stat_dict.setdefault(new_id, 0)
        t = threading.Thread(target=servant, args=(new_id,))
        t.start()
        threads.append(t)

    # start consumer threads
    consumer_name_prefix = 'CONSUMER-'
    consumer_count = 0
    consumer_indent = '+' * 2

    for i in range(num_of_consumers):
        consumer_count += 1
        new_id = consumer_name_prefix + str(consumer_count).rjust(2, '0')
        consumer_stat_dict.setdefault(new_id, 0)
        t = threading.Thread(target=consumer, args=(new_id,))
        t.start()
        threads.append(t)

    # block until all tasks are done
    product_queue.join()
    order_queue.join()

    # stop workers
    for i in range(num_of_producers + num_of_servants):
        product_queue.put(None)

    for i in range(num_of_consumers):
        order_queue.put(None)

    for t in threads:
        t.join()

except KeyboardInterrupt as msg:
    print(msg)

finally:

    # start summary section
    print()
    print('-' * 80)

    # calculate total time-cost for processing
    time_cost = time.monotonic() - started_at
    print(f"Total cost time: {time_cost:.2f} second(s)")

    # statistics of inventory count for each servant
    print()
    print(' Statistics of inventory count for each servant '.center(50, '-'))
    for k, v in servant_stat_dict.items():
        print("   * {0} {1}".format(str(k).ljust(20, '.'), str(v).rjust(3)))
    print()

    # statistics of consume count for each consumer
    print(' Statistics of consume count for each consumer '.center(50, '-'))
    for k, v in consumer_stat_dict.items():
        print("   * {0} {1}".format(str(k).ljust(20, '.'), str(v).rjust(3)))
    print()

    # end summary section
    print('-' * 80)
