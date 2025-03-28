from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default='profile_pictures/default.png', upload_to='profile_pictures')
    gender = models.CharField(max_length=10, choices=(('Male', 'Erkak'), ('Female', 'Ayol')), default='Male')
    bio = models.TextField(default="", blank=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"  # To‘g‘ri formatlangan

class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ('follower', 'following')  # Bir user faqat bir marta follow qila oladi

    def __str__(self):
        return f"{self.follower} follows {self.following}"

