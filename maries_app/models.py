from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class service_provider(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class user(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class complaint(models.Model):
    complaint = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    USER =  models.ForeignKey(user, default=1, on_delete=models.CASCADE)

class service_type(models.Model):
    type= models.CharField(max_length=100)

class subcatogary(models.Model):
    subcatogary_name= models.CharField(max_length=100)
    SERVICE_TYPE= models.ForeignKey(service_type, default=1, on_delete=models.CASCADE)

class service(models.Model):
    descrption =models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    photo =models.CharField(max_length=100)
    SERVICE_PROVIDER =models.ForeignKey(service_provider, default=1, on_delete=models.CASCADE)
    SUBCATEGORY =models.ForeignKey(subcatogary, default=1, on_delete=models.CASCADE)

class bank(models.Model):
    bank_name = models.CharField(max_length=100)
    IFSC_code = models.CharField(max_length=100)
    account_no = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class rating(models.Model):
    rate =  models.CharField(max_length=100)
    date =  models.CharField(max_length=100)
    USER =  models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    SERVICE_PROVIDER =  models.ForeignKey(service_provider, default=1, on_delete=models.CASCADE)

class chat(models.Model):
    chat = models.CharField(max_length=100)
    type =models.CharField(max_length=100)
    date =models.CharField(max_length=100)
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    SERVICE_PROVIDER = models.ForeignKey(service_provider, default=1, on_delete=models.CASCADE)

class service_cart(models.Model):
    request_date=models.CharField(max_length=100)
    USER= models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    SERVICE= models.ForeignKey(service, default=1, on_delete=models.CASCADE)

class request_service(models.Model):
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    payment_date = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    USER= models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    SERVICE_PROVIDER= models.ForeignKey(service_provider, default=1, on_delete=models.CASCADE)

class request_sub(models.Model):
    request_date = models.CharField(max_length=100)
    SERVICE = models.ForeignKey(service, default=1, on_delete=models.CASCADE)
    REQUEST = models.ForeignKey(request_service, default=1, on_delete=models.CASCADE)


class feed_back(models.Model):
    date=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)