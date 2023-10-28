from re import S


class NextNumber():
    def __init__(self, initial_value, stop_value) -> None:
        self.accum = initial_value
        self.stop_value = stop_value


    def __iter__(self):
        return self
    
    
    def __next__(self):
        x = self.accum
        self.accum += 1
        if x <= self.stop_value:
            return x  
        else:
            raise StopIteration
           

