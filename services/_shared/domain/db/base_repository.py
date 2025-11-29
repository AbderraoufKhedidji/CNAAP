class BaseRepository:
    def __init__(self, model, db):
        self.model = model
        self.db = db

    def get(self, id):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def all(self):
        return self.db.query(self.model).all()

    def filter(self, *criterion):
        return self.db.query(self.model).filter(*criterion).all()

    def add(self, entity):
        self.db.add(entity)
        return entity

    def delete(self, entity):
        self.db.delete(entity)