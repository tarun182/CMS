from django.db import models

class items(models.Model):
    Component_Name=models.CharField(max_length=200, blank=True)
    Compo_CHOICES = (
        ('Laptops', 'Laptops'),
        ('Storage', 'storage'),
        ('Mobiles', 'Mobiles'),
        ('Fashion', 'Fashion'),
    )
    Component_Type=models.CharField(max_length=10, choices=Compo_CHOICES, blank=True)
    STATUS_CHOICES = (
        ('FREE', 'Free'),
        ('IN USE', 'In use'),
    )
    Status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    Network_ID = models.CharField(max_length=200,primary_key=True, blank=True)
    Condition_CHOICES = (
        ('USABLE', 'Usable'),
        ('FAULTY', 'faulty'),
    )
    Condition = models.CharField(max_length=10, choices=Condition_CHOICES, blank=True)
    

    def __str__(self):
        return self.Component_Name

    class Meta:
        verbose_name_plural="items"



