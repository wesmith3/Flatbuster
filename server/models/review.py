from app_setup import (
    SerializerMixin, 
    metadata, 
    association_proxy, 
    validates,
    db)

class Review(db.Model, SerializerMixin):
    __tablename__='reviews'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    rental_id = db.Column(db.Integer, db.ForeignKey('rentals.id'))
    
    def __repr__(self):
        return f"<User {self.id} {self.comment} {self.rating} employed:{self.date}>"