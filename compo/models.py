from django.db import models

class items(models.Model):
    component_name=models.CharField(max_length=200, blank=True)
    Compo_CHOICES = (
        ('L', 'Laptops'),
        ('S', 'Storage'),
        ('M', 'Mobiles'),
        ('F', 'Fashion'),
    )
    Component_Type=models.CharField(max_length=1, choices=Compo_CHOICES, blank=True)
    STATUS_CHOICES = (
        ('Y', 'Free'),
        ('N', 'In use'),
    )
    Status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    Network_ID = models.CharField(max_length=200, blank=True)
    Condition_CHOICES = (
        ('U', 'Usable'),
        ('F', 'faulty'),
    )
    Condition = models.CharField(max_length=1, choices=Condition_CHOICES, blank=True)
    

    def __str__(self):
        return self.component_name

    class Meta:
        verbose_name_plural="items"



