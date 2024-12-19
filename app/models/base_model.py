
class BaseModel:
    def __init__(self):
        self.data = {}
        self.counter = 1

    def create(self, obj):
        obj['id'] = self.counter
        self.data[self.counter] = obj
        self.counter += 1
        return obj

    def get_all(self):
        return list(self.data.values())

    def get_by_id(self, obj_id):
        return self.data.get(obj_id)

    def update(self, obj_id, updated_fields):
        if obj_id not in self.data:
            return None
        self.data[obj_id].update(updated_fields)
        return self.data[obj_id]

    def delete(self, obj_id):
        return self.data.pop(obj_id, None)
