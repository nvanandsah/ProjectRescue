from django.db import models

class UserDetail(models.Model):
    name=models.CharField(max_length=250)
    phone_number=models.CharField(max_length=50)
    firebase_token = models.TextField(default=None, null=True)
    detail=models.TextField()
    
class Message(models.Model):
    user=models.ForeignKey(UserDetail,on_delete=models.CASCADE)
    message=models.TextField()
    added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (str(self.user.name)+' (' + str(self.user.phone_number)+') --> ' + str(self.message))
