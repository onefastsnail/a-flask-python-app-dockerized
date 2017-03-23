from app import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)

    __tablename__ = 'notes'

    def __init__(self, title, body):
        self.title = title
        self.body = body