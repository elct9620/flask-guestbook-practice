from app import db


class Comment(db.Model):
    """
    Comment
    """

    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    content = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.now())
