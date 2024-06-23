from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=11)
    #profile_photo = models.ImageField(blank=True, upload_to='profile_images/')
    user_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    productName = models.CharField(max_length=100)
    price = models.IntegerField()
    productImg = models.ImageField(blank=True, null=True, upload_to='item_images/')
    startDate = models.DateField()
    endDate = models.DateField()
    sellerId = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=500, default='http://example.com')
    
    def __str__(self):
        return self.productName
    
# class LikeList(models.Model):
#     Like=models.BooleanField(default=False)
#     User=models.ForeignKey(User,on_delete=models.CASCADE)
#     Item=models.ForeignKey(Item,on_delete=models.CASCADE)
    
    
#     def __str__(self):
#         return f'{self.User.sellerName} likes {self.Item.productName}'