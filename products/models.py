from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    likes_count = models.PositiveIntegerField(default=0)  # 좋아요 수를 저장할 필드

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f'{self.user.username} likes {self.product.title}'