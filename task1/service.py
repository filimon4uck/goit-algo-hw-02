import queue
from order import Order
import time
import random
import shortuuid


def generate_order(orders_queue, id, status):
    order = Order(id)
    order.status = status
    orders_queue.put(order)
    print(f"Order {order.id}, status: {order.status} was added")


def process_order(orders_queue):
    if not orders_queue.empty():
        order = orders_queue.get()
        order.status = "Finished"
        print(f"Order {order.id}, status: {order.status} was deleted")

    else:
        print("Queue is empty")


def main():
    orders_queue = queue.Queue()
    try:
        while True:
            time.sleep(1)
            if random.choice([True, False]):
                generate_order(orders_queue, shortuuid.uuid(), "Created")
            if random.choice([True, False]):
                process_order(orders_queue)
    except KeyboardInterrupt:
        print("Application was finished user")


if __name__ == "__main__":
    main()
