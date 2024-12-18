from copy import deepcopy


class DeltaFloat:
    """
    Handle deltas for float variables
    """
    @staticmethod
    def create(old: float, new: float):
        """
        Create delta for float variable
        """
        return deepcopy(new) - deepcopy(old)
    
    @staticmethod
    def apply(old: float, delta: float):
        """
        Apply delta to the float variable
        """
        return deepcopy(old) + deepcopy(delta)
    

if __name__ == "__main__":
    old_var = 1.3
    new_var = 3.7

    delta = DeltaFloat.create(old_var, new_var)
    print(delta) # expected: 2.4

    var = DeltaFloat.apply(old_var, delta)
    print(var) # expected: 3.7