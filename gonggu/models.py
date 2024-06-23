from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    profile_photo = models.ImageField(blank=True, upload_to='profile_images/')
    user_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_photo = models.ImageField(blank=True, upload_to='item_images/')
    start_time = models.DateField()
    end_time = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.item_name
    
    def user_name(self):
        return self.user.name

    def user_profile_photo(self):
        return self.user.profile_photo.url if self.user.profile_photo else None