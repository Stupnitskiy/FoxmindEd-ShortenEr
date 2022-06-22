from src import db


class Link(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), nullable=False)
    short_id = db.Column(db.String(255), nullable=False)
    views_amount = db.Column(db.Integer, nullable=False)

    def __init__(self, original_url, short_id, views_amount):
        self.original_url = original_url
        self.short_id = short_id
        self.views_amount = views_amount
