from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe
from PIL import Image

class PasswordResetRequest(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   token = models.CharField(max_length=43, default=token_urlsafe)
   created_timestamp = models.DateTimeField(auto_now_add=True)
   updated_timestamp = models.DateTimeField(auto_now=True)

   def __str__(self):
      return f'{self.user} - {self.created_timestamp} - {self.updated_timestamp} - {self.token}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)