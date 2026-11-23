
import gc
import time

class Node:
    def __init__(self, name):
        self.name = name
        self.reference = None

    def __del__(self):
        print(f"Object {self.name} destroyed")

def show_gc_info():
    print("\nGarbage Collector Information")
    print("GC Enabled:", gc.isenabled())
    print("GC Threshold:", gc.get_threshold())
    print("GC Count:", gc.get_count())

def create_garbage():
    print("\nCreating circular references...")

    obj1 = Node("A")
    obj2 = Node("B")

    obj1.reference = obj2
    obj2.reference = obj1

    print("Circular references created successfully!")

    del obj1
    del obj2

    print("Object references deleted.")


def manual_collection():
    print("\nStarting manual garbage collection...")

    collected = gc.collect()

    print("Garbage objects collected:", collected)
    print("Garbage remaining:", len(gc.garbage))

def main():
    print("AUTOMATIC GARBAGE COLLECTION DEMO")

    show_gc_info()

    print("\nAutomatic GC Status:", gc.isenabled())

    create_garbage()

    print("\nWaiting for garbage collection...")
    time.sleep(1)

    manual_collection()

    print("\nFinal GC Information")
    show_gc_info()

    print("\nGarbage collection experiment completed!")

if __name__ == "__main__":
    main()
