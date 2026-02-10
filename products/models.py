from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
#category of products
class category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='img/banner/')
    def __str__(self):
        return self.name
class category_1(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='img/banner/')
    def __str__(self):
        return self.name
class category_2(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='img/banner/')
    def __str__(self):
        return self.name
# Create your models here.
class sale_of(models.Model):
    title=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='img/product_sale')
    price=models.CharField(max_length=50)
    day= models.DateField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name
class instagram(models.Model):
    image_1=models.ImageField(upload_to='img/instagram')
    image_2=models.ImageField(upload_to='img/instagram')
    image_3=models.ImageField(upload_to='img/instagram')
    image_4=models.ImageField(upload_to='img/instagram')
    image_5=models.ImageField(upload_to='img/instagram')
    image_6=models.ImageField(upload_to='img/instagram')
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class latest_news(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=200)
    image_1=models.ImageField(upload_to='img/blog')
    date_1=models.CharField(max_length=50)
    description_1=models.CharField(max_length=100)
    image_2=models.ImageField(upload_to='img/blog')
    description_2=models.CharField(max_length=100)
    date_2=models.CharField(max_length=50)
    image_3=models.ImageField(upload_to='img/blog')
    description_3=models.CharField(max_length=100)
    date_3=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class newletter(models.Model):
    email=models.EmailField(max_length=50)
    def __str__(self):
        return self.email
class contact_us_message(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    message=models.CharField(max_length=300)
    def __str__(self):
        return self.name
class index_collection(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    image_1=models.ImageField(upload_to='img/hero/')
    image_2=models.ImageField(upload_to='img/hero/')
    def __str__(self):
        return self.name
class logo(models.Model):
    logo_1=models.ImageField(upload_to='img/')
    logo_2=models.ImageField(upload_to='img/')
    logo_3=models.ImageField(upload_to='img/')

class Product(models.Model):
    STOCK=('SALE','SALE'),('NEW','NEW'),('OUT OF STOCK','OUT OF STOCK')
    unique_id=models.CharField(unique=True,max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='img/product/')
    name=models.CharField(max_length=200)
    price=models.FloatField()
    digital=models.BooleanField(default=False,null=True,blank=True)
    description=models.CharField(max_length=250)
    stock=models.CharField(choices=STOCK,max_length=20)
    created_date=models.DateTimeField(default=timezone.now)
    def save(self,*args,**kwaargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id=self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwaargs)
    def __str__(self):
        return self.name
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    profile_img=models.ImageField(default='img/profile/default1.png',upload_to='img/profile/',null=True,blank=True)
    def __str__(self):
        return str(self.name)
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=True)
    transaction_id=models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)
    @property
    def shipping(self):
        shipping=False
        orderitems=self.order_items.all()
        for i in orderitems:
            if i.product.digital==False:
                shipping=True

        return shipping
    
    @property
    def get_cart_total(self):
        orderitems=self.order_items.all()
        total=sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems=self.order_items.all()
        total=sum([item.quantity for item in orderitems])
        return total
   

   

    
class Order_item(models.Model):
     product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
     order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True, related_name='order_items')
     quantity=models.IntegerField(default=0,null=True,blank=True)
     date_added=models.DateTimeField(auto_now_add=True)
     @property
     def get_total(self):
        total=self.product.price * self.quantity
        return total
     def __str__(self):
        return str(self.product)
    

class shippingAddress(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    state=models.CharField(max_length=200,null=True)
    zipcode=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id)


class contact_us_view(models.Model):
    title_1=models.CharField(max_length=200)
    description_1=models.CharField(max_length=200)
    title_2=models.CharField(max_length=200)
    description_2=models.CharField(max_length=250)
    title_3=models.CharField(max_length=200)
    description_3=models.CharField(max_length=250)
    phone_1=models.CharField(max_length=50)
    phone_2=models.CharField(max_length=50)
    def __str__(self):
        return self.title_1
class leave_comment(models.Model):
    title=models.CharField(max_length=50)
    date_added=models.DateTimeField(auto_now_add=True)
    image_title=models.ImageField(upload_to='img/blog/details')
    description_1=models.CharField(max_length=500)
    description_2=models.CharField(max_length=300)
    writer_name=models.CharField(max_length=20)
    image_writer=models.ImageField(upload_to='img/blog/details')
    hashtag_1=models.CharField(max_length=20)
    hashtag_2=models.CharField(max_length=20)
    hashtag_3=models.CharField(max_length=20)
    def __str__(self):
        return self.title
class send_comment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    comment=models.CharField(max_length=1000)
    def __str__(self):
        return self.name
class aboutus(models.Model):
    name=models.CharField(max_length=10)
    image=models.ImageField(upload_to='img/about/')
    title_1=models.CharField(max_length=50)
    description_1=models.CharField(max_length=500)
    title_2=models.CharField(max_length=50)
    description_2=models.CharField(max_length=500)
    title_3=models.CharField(max_length=50)
    description_3=models.CharField(max_length=500)
    blog_description=models.CharField(max_length=1000)
    blog_img=models.ImageField(upload_to='img/about/')
    author_name=models.CharField(max_length=50)
    author_img=models.ImageField(upload_to='img/about/')
    author_department=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class team_members(models.Model):
    
    name=models.CharField(max_length=50)
    img=models.ImageField(upload_to='img/about/')
    department=models.CharField(max_length=100)
    def __str__(self):
        return self.name