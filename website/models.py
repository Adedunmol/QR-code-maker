from website import db


class UserUrl(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    url = db.Column(db.String(50))
    image = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.id}, {self.image}'
