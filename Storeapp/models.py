from django.db import models
# models.py în aplicația Storeapp
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# class CardData(models.Model):
#
#  card_number =
#     card_owener=
#     cvv_code =
#     year_expiration =
#     month_expiration  =


class ShoppingCartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} - {self.user.username}"


class CardData(models.Model):
    card_number = models.CharField(max_length=16)
    card_owner = models.CharField(max_length=100)
    cvv_code = models.CharField(max_length=4)
    year_expiration = models.IntegerField()
    month_expiration = models.IntegerField()

    def __str__(self):
        return f"Card: {self.card_number} - Owner: {self.card_owner}"

