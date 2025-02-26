from django.db import models
from django.utils.timezone import now  # ✅ Import timezone-aware now()


class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category= models.CharField(max_length=50, default="")
    sub_category= models.CharField(max_length=50, default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField(default=2025-11-22)
    image= models.ImageField(upload_to="shop/images",default="")