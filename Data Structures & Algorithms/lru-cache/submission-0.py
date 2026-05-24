class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity


    def get(self, key: int) -> int:
        #need to look for a key in a hashmap 
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        #put will be pretty easy to run in O(1)
        #because its just adding to the end and replacing 
        #the front         
        if key in self.cache: 
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        if len(self.cache) > self.cap: 
            self.cache.popitem(last = False) 
