class HashTable:
   def __init__(self, size):
       self.size = size
       self.table = [[] for _ in range(size)]
   def hash_function(self, key):
       return hash(key) % self.size
   def insert(self, key, value):
       index = self.hash_function(key)
       for item in self.table[index]:
           if item[0] == key:
               item[1] = value  # Update value if key already exists
               return
       self.table[index].append([key, value])  # Add new key-value pair
   def get(self, key):
       index = self.hash_function(key)
       for item in self.table[index]:
           if item[0] == key:
               return item[1]  # Return value if key is found
       return None  # Return None if key is not found

# Usage example
hash_table = HashTable(10)
hash_table.insert("apple", 10)
hash_table.insert("banana", 5)
hash_table.insert("orange", 8)
hash_table.insert("apple", 15)  # Updating existing key

print(hash_table.get("apple"))  # Output: 15
print(hash_table.get("banana"))  # Output: 5
print(hash_table.get("grape"))  # Output: None
