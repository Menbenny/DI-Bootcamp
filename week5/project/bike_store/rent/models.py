from django.db import models

# Create your models here.

def customer(first_name, last_name, email, phone_number, address, city, country):
    fisrt_name = customer.first_name
    last_name = customer.last_name
    email = customer.email
    phone_number = customer.phone_number
    address = customer.address
    city = customer.city
    country = customer.country

# vehicle_type (foreign key)
# name

def vehicle(type, cost, size):
    type = vehicle.type
    cost = vehicle.cost
    size = vehicle.size

def rental(rental_date, return_date, customer, vehicle)
    rental_date = rental.rental_date
    return_date = rental.return_date
    customer = rental.customer
    vehicle = rental.vehicle

def rental_station(name, capacity, address):
    name = rental_station.name
    capacity = rental_station.capacity
    address = rental_station.address



