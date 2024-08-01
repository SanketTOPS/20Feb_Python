from django.db import models

# Create your models here.


class product_master(models.Model): #category
    product_id = models.AutoField(primary_key=True)
    pname=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.pname

class sub_category(models.Model):
    pname=models.ForeignKey(product_master,on_delete=models.CASCADE)
    price=models.IntegerField()
    img=models.ImageField(upload_to="images")
    ram=models.IntegerField()
    pmodel=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.pname.pname



