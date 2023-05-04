from flask import session
from .base_model import BaseModel

class Joke(BaseModel):

    jokes = []
    json_fields = ['id', 'setup', 'punchline']

    def __init__(self, setup, punchline):
        self.id = len(self.jokes) + 1
        self.setup = setup
        self.punchline = punchline
        self.jokes.append(self)

    @classmethod
    def all(cls):
        return cls.jokes
    
    @classmethod
    def get_by_id(cls, id):
        return cls.jokes[id - 1]
    
    @classmethod
    def create(cls, data):
        joke = cls(**data)
        return joke
    
    @classmethod
    def update(cls, id, data):
        joke = cls.get_by_id(id)
        joke.setup = data['setup']
        joke.punchline = data['punchline']
        return joke
    
    @classmethod
    def delete(cls, id):
        joke = cls.get_by_id(id)
        cls.jokes.remove(joke)
        return True
    