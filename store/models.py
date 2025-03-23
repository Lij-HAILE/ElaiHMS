from django.db import models
from accounts.models import MyUser

type = (
    ("Thread","Thread"),
    ("Thread-3","Thread-3"),
    ("Riser","Riser"),
    ("Riser-3","Riser-3"),
    ('Windowsill',"Windowsill"),
    ('Windowsill-3',"Windowsill-3"),
    ('Doorsill',"Doorsill"),
    ('Doorsill-3',"Doorsill-3"),
    ('Landing',"Landing"),
    ('Landing-3',"Landing-3"),
    ('Coping',"Coping"),
    ('Coping-3',"Coping-3"),
    ('Skirting',"Skirting"),
    ('Skirting-3',"Skirting-3"),
)
# Create your models here.
class Table(models.Model):
    name=models.CharField(max_length=100)
class Order(models.Model):
    table =models.ForeignKey(Table,on_delete=models.SET_DEFAULT,default=1,blank=True)
    user = models.ForeignKey(MyUser,on_delete=models.SET_NULL,null=True,blank=True)
    customer = models.CharField(max_length=254)
    type = models.CharField(max_length=254,choices=type)
    length = models.FloatField()
    width=models.FloatField()
    pieces=models.IntegerField()
    ML =models.FloatField()
    SQ_M =models.FloatField()
    complete =models.IntegerField(blank=True,null=True)
    special_finish = models.CharField(max_length=254,blank=True,null=True)

    class Meta:
        ordering = ['id']
class Answer(models.Model):
    user =models.ForeignKey(MyUser,on_delete=models.CASCADE)
    ans =models.TextField()
    date =models.DateField(auto_now_add=True)
class Question(models.Model):
    user =models.ForeignKey(MyUser,on_delete=models.CASCADE)
    title =models.CharField(max_length=250)
    desc = models.TextField()
    answer = models.ManyToManyField(Answer)
    date = models.DateField(auto_now_add=True)


