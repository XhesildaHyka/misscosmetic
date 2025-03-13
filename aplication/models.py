from django.db import models

# Create your models here.


def default_image():
    return 'default.jpg'  

class CarouselImage(models.Model):
    image1 = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)
    image2 = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)
    image3 = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)

class Arrival(models.Model):
    arrival_title = models.CharField(max_length=450, null=True, blank=True)
    arrival_image = models.ImageField(upload_to="arrival/", null=True, blank=True)

    def __str__(self):
        return self.arrival_title

class Marka(models.Model):
    marka_title=models.CharField(max_length=250,null=250,blank=True)
    def __str__(self):
     return f"{self.marka_title}"

class Makeup(models.Model):
    makeup_title=models.CharField(max_length=250,null=250,blank=True)
    def __str__(self):
     return f"{self.makeup_title}"


class Skincare(models.Model):
    skincare_title=models.CharField(max_length=250,null=250,blank=True)
    def __str__(self):
     return f"{self.skincare_title}"
    
class Accessor(models.Model):
    accessor_title=models.CharField(max_length=250,null=250,blank=True)
    def __str__(self):
     return f"{self.accessor_title}"
    
class Offer(models.Model):
    discount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
     return f"{self.offer_title}"
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=450)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE, null=True, blank=True)
    marka=models.ForeignKey(Marka,on_delete=models.CASCADE,null=True,blank=True)
    makeup=models.ForeignKey(Makeup,on_delete=models.CASCADE,null=True,blank=True)
    skincare=models.ForeignKey(Skincare,on_delete=models.CASCADE,null=True,blank=True)
    accessor=models.ForeignKey(Accessor,on_delete=models.CASCADE,null=True,blank=True)
   
   

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    contact_name = models.CharField(max_length=50,null=True, blank=True)
    contact_lastname = models.CharField(max_length=50,null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_sms= models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
            return f"{self.contact_name} {self.contact_lastname}"