from .models import Customers, Films


# Fetch all customers information
def fetch_customers():
	data = Customers.objects.exclude('Rentals')
	return data


# Fetch specific customer information
def fetch_customer_info(id):
	data = Customers.objects.get(_id = id)
	return data

# Fetch all available films
def fetch_available_films():
	rentals = Customers.objects.values_list('Rentals')
	rental_films = set()
	for rental in rentals:
		for film in rental:
			rental_films.add(film['filmId'])
	data = Films.objects(id__nin=list(rental_films)).exclude('Actors', 'Length', 'ReplacementCost', 'SpecialFeatures')
	return data

# Fetch all films 
def fetch_all_films():
	data = Films.objects.exclude('Actors', 'Length', 'ReplacementCost', 'SpecialFeatures')
	return data

# Fetch film info and rental customers
def fetch_film_info(id):
	film = Films.objects.get(_id = id)
	rented_customers = Customers.objects(Rentals__filmId = int(id)).exclude('Rentals')
	data = {'film_info': film, 'rented_customers': rented_customers}
	return data
