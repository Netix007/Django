from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. "
                                         "Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'client: {self.name}, email: {self.email}, phone: {self.phone_number}, address: {self.address},' \
               f' registration date: {self.registration_date}'


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'item: {self.name}, description: {self.description}, price: {self.price}, count: {self.count},' \
               f' add_date: {self.add_date}'


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Item)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'customer_id: {self.customer}, products_id: {self.products.all()}, total_price: {self.total_price}, ' \
               f'date_ordered: {self.date_ordered}'
