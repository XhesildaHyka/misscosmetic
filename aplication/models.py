from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def default_image():
    return 'default.jpg'  

class CarouselImage(models.Model):
    image1 = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)
    image = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)
    image3 = models.ImageField(upload_to='carousel_images/', blank=True, null=True, default=default_image)

class Arrival(models.Model):
    arrival_title = models.TextField(max_length=450,null=True, blank=True)
    arrival_image = models.ImageField(upload_to="arrival/", null=True, blank=True )
    def __str__(self):
        return f"{self.arrival_title}"

class Collection(models.Model):
    collection_title = models.TextField(max_length=450,null=True, blank=True)
    collection_image = models.ImageField(upload_to="collection/", null=True, blank=True )
    def __str__(self):
        return f"{self.collection_title}"
    
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
    offer_title= models.CharField(max_length=250,null=True,blank=True)
    offer_image = models.ImageField(upload_to="offer/", null=True, blank=True )

    def __str__(self):
     return f"{self.offer_title}"
    

    
class Video(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    

    def __str__(self):
        # Ensure that the __str__ method returns a string
        return self.title if self.title else 'Untitled Video'

class Product(models.Model):
  
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True)
    actual_price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    arrival = models.ForeignKey(Arrival, on_delete=models.CASCADE, null=True, blank=True)
    marka=models.ForeignKey(Marka,on_delete=models.CASCADE,null=True,blank=True)
    makeup=models.ForeignKey(Makeup,on_delete=models.CASCADE,null=True,blank=True)
    skincare=models.ForeignKey(Skincare,on_delete=models.CASCADE,null=True,blank=True)
    accessor=models.ForeignKey(Accessor,on_delete=models.CASCADE,null=True,blank=True)
    offer=models.ForeignKey(Offer,on_delete=models.CASCADE,null=True,blank=True)
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE,null=True,blank=True)
    is_bestseller = models.BooleanField(default=False)

   
   
    def __str__(self):
        return self.name
    


    
class Contact(models.Model):
    contact_name = models.CharField(max_length=50,null=True, blank=True)
    contact_lastname = models.CharField(max_length=50,null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_sms= models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
            return f"{self.contact_name} {self.contact_lastname}"
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.quantity} x {self.item.name} (User: {self.user})"
    
    def get_total(self):
        total = self.item.actual_price * self.quantity
        float_total = format(total, '0.2f')
        return float_total


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    orderitems = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.created}'

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total
