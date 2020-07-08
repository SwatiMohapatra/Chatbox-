from django.db import models

# Create your models here.
class Complaint(models.Model):
    category = models.CharField(max_length=30, null=True)
    sub_category = models.CharField(max_length=30, null=True)
    subject = models.CharField(max_length=50, null=True)
    complain_1 = models.TextField(null=True)

    def __str__(self):
        return str(self.category)

class Studentmsg(models.Model):
    studmsg = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.studmsg)

class Membermsg(models.Model):
    membmsg = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.membmsg)
