from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.customer_name} - {self.service.name}"
