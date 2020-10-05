from flask import jsonify, Blueprint, request
from app.database.db import fetch_customers, fetch_customer_info, fetch_available_films, fetch_all_films, fetch_film_info
import math
import datetime

blueprint = Blueprint('all_customers', __name__)


@blueprint.route('/all_customers', methods=['GET'])
def all_customers():
	all_customers = fetch_customers()
	return jsonify(all_customers)


@blueprint.route('/customer_info', methods=['POST'])
def customer_info():
	id = request.form.get('id')
	data = fetch_customer_info(id)
	rentals = data.Rentals
	for idx, rental in enumerate(rentals):
		rental_start = datetime.datetime.strptime(rental['Rental Date'], '%Y-%m-%d %H:%M:%S.%f')
		rental_end = datetime.datetime.strptime(rental['Return Date'], '%Y-%m-%d %H:%M:%S.%f')
		rented_days = (rental_end - rental_start).days + (1 if (rental_end - rental_start).seconds > 0 else 0)

		updated_rental = {
			'Rental Date': rental['Rental Date'],
			'Rental Duration': rented_days,
			'Cost': sum([payment['Amount'] for payment in rental['Payments']])
		}
		data.Rentals[idx] = updated_rental

	return jsonify(data)


@blueprint.route('/available_films', methods=['GET'])
def available_films():
	data = fetch_films()
	return jsonify(data)


@blueprint.route('/all_films', methods=['GET'])
def all_films():
	data = fetch_all_films()
	return jsonify(data)

@blueprint.route('/film_info', methods=['POST'])
def film_info():
	id = request.form.get('id')
	data = fetch_film_info(id)
	return jsonify(data)