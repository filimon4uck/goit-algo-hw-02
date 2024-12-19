import queue
import time
import random


def generate_order(orders_queue, id):
    orders_queue.put({id})
    print(f"Order {id} was added")


def process_order(orders_queue):
    if not orders_queue.empty():
        order = orders_queue.get()
        print(f"Order {order} was deleted")

    else:
        print("Queue is empty")


def main():
    orders_queue = queue.Queue()
    try:
        id = 1
        while True:
            time.sleep(1)
            if random.choice([True, False]):
                generate_order(orders_queue, id)
                id += 1
            if random.choice([True, False]):
                process_order(orders_queue)
    except KeyboardInterrupt:
        print("Application was finished user")


if __name__ == "__main__":
    main()
