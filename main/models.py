from django.db import models

class Post(models.Model):
    title = models.CharField("Sarlavha", max_length=200)
    content = models.CharField("Matn")
    time = models.DateTimeField("Yaratilgan sana", auto_now_add=True)
    def __str__(self):
        return self.title
    
    