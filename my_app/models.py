from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class agriculture_office(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)

class user(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class feedback(models.Model):
    feedback = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user,on_delete=models.CASCADE,default=1)

class complaint(models.Model):
    complaint = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class notification_office(models.Model):
    notification = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    AGRICULTURE_OFFICE = models.ForeignKey(agriculture_office, on_delete=models.CASCADE, default=1)

class fertilizer(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    AGRICULTURE_OFFICE = models.ForeignKey(agriculture_office, on_delete=models.CASCADE, default=1)

class notification(models.Model):
    notifications = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

class success_story(models.Model):
    notes = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    AGRICULTURE_OFFICE = models.ForeignKey(agriculture_office, on_delete=models.CASCADE, default=1)

class stock(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    AGRICULTURE_OFFICE = models.ForeignKey(agriculture_office, on_delete=models.CASCADE, default=1)

class orders(models.Model):
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    # status = models.CharField(max_length=100)
    AGRICULTURE_OFFICE = models.ForeignKey(agriculture_office, on_delete=models.CASCADE, default=1)
    # STOCK = models.ForeignKey(stock, on_delete=models.CASCADE, default=1)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class order_sub(models.Model):
    quantity = models.CharField(max_length=100)
    STOCK = models.ForeignKey(stock, on_delete=models.CASCADE, default=1)
    ORDERS = models.ForeignKey(orders, on_delete=models.CASCADE, default=1)

class cart(models.Model):
    quantity = models.CharField(max_length=100)
    STOCK = models.ForeignKey(stock, on_delete=models.CASCADE, default=1)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class chat(models.Model):
    chat = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    AGRICULTURE_OFFICE = models.ForeignKey(agriculture_office, on_delete=models.CASCADE, default=1)

class subsidy(models.Model):
    item_name = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    From = models.CharField(max_length=100)
    To = models.CharField(max_length=100)







