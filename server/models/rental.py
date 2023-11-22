from app_setup import (
    SerializerMixin, 
    metadata, 
    association_proxy, 
    validates,
    db)





class Rental(db.Model, SerializerMixin):
    __tablename__="rentals"
    
    id = db.Column(db.Integer, primary_key = True)
    rental_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    
    def __repr__(self):
        return f"<User {self.id} {self.rental_date} {self.return_date} >"