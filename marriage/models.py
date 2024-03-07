from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type  = models.CharField(max_length=50)

class service_provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    lattitude = models.CharField(max_length=100,default=2)
    longitude = models.CharField(max_length=100,default=2)

    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)

class user(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class complaint(models.Model):
    complaints = models.CharField(max_length=100)
    complaint_date = models.CharField(max_length=100)
    reply = models.CharField(max_length=50)
    reply_date = models.CharField(max_length=50)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)

class service_type(models.Model):
    type = models.CharField(max_length=100)

class subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    SERVICE_TYPE = models.ForeignKey(service_type, on_delete=models.CASCADE, default=1)

class service(models.Model):
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    SERVICE_PROVIDER = models.ForeignKey(service_provider, on_delete=models.CASCADE, default=1)
    SUBCATEGORY = models.ForeignKey(subcategory, on_delete=models.CASCADE, default=1)

class bank(models.Model):
    bank_name = models.CharField(max_length=100)
    IFSC_code = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)

class rating(models.Model):
    rate = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    SERVICE_PROVIDER = models.ForeignKey(service_provider, on_delete=models.CASCADE, default=1)

class chat(models.Model):
    chat = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    SERVICE_PROVIDER = models.ForeignKey(service_provider, on_delete=models.CASCADE, default=1)

class service_cart(models.Model):
    request_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    SERVICE = models.ForeignKey(service,on_delete=models.CASCADE,default=1)

class req(models.Model):
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    payment_date = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)
    SERVICE_PROVIDER = models.ForeignKey(service_provider, on_delete=models.CASCADE, default=1)

class req_sub(models.Model):
    request_date = models.CharField(max_length=100)
    SERVICE = models.ForeignKey(service, on_delete=models.CASCADE, default=1)
    REQUEST = models.ForeignKey(req,on_delete=models.CASCADE,default=1)














