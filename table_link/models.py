from django.db import models

# Create your models here.







class Category(models.Model):
    categorty = models.CharField(max_length=50)


    def __str__(self):
        return self.categorty


class Books(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    janre =models.ForeignKey(Category,null=True,blank=True, on_delete=models.PROTECT)
    info = models.TextField()
    Date_of_issue = models.DateField()

    def __str__(self):
        return self.name, self.author, self.janre






