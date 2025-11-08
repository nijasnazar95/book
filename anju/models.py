from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    covers=models.ImageField(upload_to="upload",blank=True , null=True)

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    book=models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    def _str_(self):
        return f"{self.quantity} x {self.book.name}  by {self.book.author}"