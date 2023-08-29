from django.db import models


# --------------- USER -----------------------------------------------------------------------
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    us_adrs = models.CharField(max_length=100)
    reg_day = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}  -  {self.mobile} '

    def full_data(self):
        return f'{self.name}  -  ' \
               f'{self.mobile}<br>' \
               f'{self.email} <br>' \
               f'{self.us_adrs} <br>' \
               f'{self.reg_day}'


# -------------- PRODUCT -----------------------------------------------------------------------
class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(default=1000.0, decimal_places=2, max_digits=10)
    count = models.IntegerField(default=1)
    add_day = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}  -  {self.price} '

    def full_data(self):
        return f'{self.name}  -  {self.price} <br>' \
               f'{self.content}<br>' \
               f'Count: {self.count}   Added at: {self.add_day}<br>'

    def price_get(self):
        return self.price


# -------------- ORDER -----------------------------------------------------------------------
class Order(models.Model):
    us_name = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name="order_products")
    sum_price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    order_day = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.us_name}' \
               f'Sum price: {self.sum_price}' \
               f'Date: {self.order_day}' \
               # f'{self.products}'
