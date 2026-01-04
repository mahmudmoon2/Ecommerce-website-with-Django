from django.db import models
from django.utils.text import slugify
from accounts.models import CustomUser
# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        

class Category(TimeStampedModel):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(blank= True , unique= True)
    image = models.ImageField(upload_to='categories')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Category name : {self.name}"
        
class Product (TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255 , unique= True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2)
    
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    unit = models.CharField(max_length=100, null=True, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    
    category = models.ForeignKey(Category, related_name='products' , on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
class ProductImage (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name='images')
    image = models.ImageField(upload_to = 'products/images')
    
    def __str__(self):
        return f"Image for {self.product.name}"
    
    
class Review(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    
    rating = models.FloatField()
    review = models.TextField()
    
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Review by{self.user.username} for {self.product.name}"
    