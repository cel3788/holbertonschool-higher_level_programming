def to_json(self, attrs=None):
    """Get a dictionary representation of the Student.
    
    If attrs is a list of strings, represents only those attributes
    included in the list.
    
    Args:
        attrs (list): (Optional) The attributes to represent.
    """
    if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
    return self.__dict__
