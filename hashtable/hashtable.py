class Node:
    def __init__(self,  key, value):
        self.value = value
        self.next = None
        self.key = key

    def __str__(self):
        return f"value: {self.value}, next: {self.next}"


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        currStr = ""
        curr = self.head
        while curr != None:
            currStr += f'{str(curr.value)} ->'
            curr = curr.next
        return currStr

    # return node w/ value
    # runtime: O(n) where n = number nodes
    def find(self, key):
        curr = self.head
        while curr != None:
            if curr.key == key:
                return curr
            curr = curr.next
        return None

    # deletes node w/ given value then return that node
    # runtime: O(n) where n = number of nodes
    def delete(self, key):
        curr = self.head

        # special case if we need to delete the head
        if curr.key == key:
            self.head = curr.next
            curr.next = None
            return curr

        prev = None

        while curr != None:
            if curr.key == key:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    # insert node at head of list
    # runtime: O(1)
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node

    # overwrite node or insert node at head
    # runtime: O(n)
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.value)  # O(n)
        if existingNode != None:
            existingNode.value = node.value
        else:
            self.insert_at_head(node)  # O(1)


MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.store = [None] * capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        num_elem = len([elem for elem in self.store if elem is not None])
        return num_elem / self.capacity

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
            # the modulus keeps it 32-bit, python ints don't overflow
            hash = ((hash * 33) ^ byte) % 0x100000000

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        elem = self.store[self.hash_index(key)]
        newEntry = Node(key, value)
        if elem is None:
            ll = LinkedList()
            ll.insert_at_head_or_overwrite(newEntry)
            self.store[self.hash_index(key)] = ll

        else:
            elem.insert_at_head_or_overwrite(newEntry)

        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        elem = self.store[self.hash_index(key)]
        if elem is not None:
            deleted_elem = elem.delete(key)
            if self.store[self.hash_index(key)].head is None:
                self.store[self.hash_index(key)] = None
            return deleted_elem
        else:
            return "key not found"

        if self.get_load_factor() < 0.2:
            new_capacity = self.capacity // 2

            if new_capacity < MIN_CAPACITY:
                new_capacity = MIN_CAPACITY

            self.resize(new_capacity)

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        elem = self.store[self.hash_index(key)]
        if elem is not None:
            return elem.find(key).value
        else:
            return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_store = self.store

        self.capacity = new_capacity
        self.store = [None] * new_capacity

        for item in old_store:
            if item:
                while item.head:
                    self.put(item.head.key, item.head.value)
                    item.delete(item.head.key)

                item = None


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
