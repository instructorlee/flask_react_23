# This class should be extended to take advantage of the to_json() method as well as any other common methods that you may want to use in your models.
class BaseModel:

    json_fields = [] 

    """
     The jsonify method used in your controller cannot convert a class object to JSON. 
     So, before returning the object to the React app, we need to convert it to a dictionary.
    """
    def to_json(self):
        return {field: getattr(self, field) for field in self.json_fields}