from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser




class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile=models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_bedrooms = models.IntegerField()
    likes = models.ManyToManyField(User, related_name='house_likes', blank=True)
    comments = models.ManyToManyField('Comment', related_name='house_comments', blank=True)
    picture = models.ImageField(upload_to='house_pics/', blank=True, null=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.house.name}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} likes {self.house.name}'
