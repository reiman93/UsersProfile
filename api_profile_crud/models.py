from django.db import models

# Create your models here.

class Profile(models.Model):
 #   img 		 = models.ImageField(upload_to='Images/', default='', blank='')
    first_name 	 = models.CharField(max_length=150)
    last_name 	 = models.CharField(max_length=150)
    phone        = models.TextField()
    address      = models.TextField()
    city         = models.CharField(max_length=150)
    state        = models.CharField(max_length=150)
    zipcode      = models.IntegerField()
    available    = models.BooleanField()
 #   profiles     = models.ForeignKey('self', null=True, related_name="profiles")
    
    
    def __str__(self):
	    return self
 
 #   def image_img(self):
 #       if self.item_image:
 #           return u'<img src="%s" width="50" height="50" />' % self.img.url
 #       else:
 #           return '(not image)' 

class Interaction(models.Model):
    profile_left=   models.ForeignKey(Profile, null=True, related_name="profile_left",on_delete=models.CASCADE)
    profile_right=  models.ForeignKey(Profile, null=True, related_name="profile_right",on_delete=models.CASCADE)
    
    def __str__(self):
	    return self