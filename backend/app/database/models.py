from app.database import db_engine as db

class Customers(db.Document):
	# Meta variables.
	meta = {
		'collection': 'customers'
	}

	# Document variables.
	_id = db.IntField(required=True)
	Address = db.StringField(required=True)
	City = db.StringField(required=True)
	Country = db.StringField(required=True)
	District = db.StringField(required=True)
	FirstName = db.StringField(db_field='First Name', required=True)
	LastName = db.StringField(db_field='Last Name', required=True)
	Phone = db.StringField(required=True)
	Rentals = db.ListField(db.DictField(), required=False)

class Films(db.Document):
	# Meta variables.
	meta = {
		'collection': 'films'
	}

	# Document variables.
	_id = db.IntField(required=True)
	Actors = db.ListField(db.DictField(), required=True)
	Category = db.StringField(required=True)
	Description = db.StringField(required=True)
	Length = db.StringField(required=True)
	Rating = db.StringField(required=True)
	RentalDuration = db.StringField(db_field='Rental Duration', required=True)
	ReplacementCost =  db.StringField(db_field='Replacement Cost', required=True)
	SpecialFeatures = db.StringField(db_field='Special Features', required=True)
	Title = db.StringField(required=True)