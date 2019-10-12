from django.db import models

# Create your models here.

class Routes(models.Model):
	stage = models.CharField(max_length = 100)
	route = models.CharField(max_length = 400)

	def __str__(self):
		return self.stage+self.route


class Stop(models.Model):
	STOP_TYPES = (
		('A', 'All'),
		('O', 'Ordinary'),
	)
	name = models.CharField(max_length = 30)
	buses_that_stop_here = models.CharField(max_length = 1, choices = STOP_TYPES)

	def __str__(self):
		return self.name


class Route(models.Model):
	number = models.CharField(max_length = 10, primary_key = True)
	stops = models.ManyToManyField(Stop)

	def __str__(self):
		return self.number


class Bus(models.Model):
	BUS_TYPES = (
		('AC', 'Air Conditioned'),
		('DE', 'Deluxe'),
		('EX', 'Express'),
		('OR', 'Ordinary'),
		('SM', 'Small'),
	)

	license_plate = models.CharField(max_length = 10, primary_key = True)
	route = models.ForeignKey('Route', on_delete = models.PROTECT)
	bus_type = models.CharField(max_length = 2, choices = BUS_TYPES)

	def __str__(self):
		return self.license_plate


class LocationHistory(models.Model):
	license_plate = models.ForeignKey('Bus', on_delete = models.CASCADE)
	lattitude = models.CharField(max_length = 20)
	longitude = models.CharField(max_length = 20)
	passengers = models.IntegerField('Number of passengers')

	def __str__(self):
		return self.license_plate.license_plate + ' | ' + self.lattitude + ', ' + self.longitude


class CurrentLocation(models.Model):
	license_plate = models.CharField(max_length = 10, primary_key = True)
	lattitude = models.CharField(max_length = 20)
	longitude = models.CharField(max_length = 20)
	passengers = models.IntegerField('Number of passengers')

	def __str__(self):
		return self.license_plate + ' | ' + self.lattitude + ', ' + self.longitude
