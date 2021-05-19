from django.db import models

#custom model manager django
class BookActiveManager(models.Manager):    #coustom manager
    def get_queryset(self):
        return super(BookActiveManager,self).get_queryset().filter(is_deleted='N')

class BookInactiveManager(models.Manager):    
    def get_queryset(self):
        return super(BookInactiveManager,self).get_queryset().filter(is_deleted='Y')

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    qty = models.IntegerField()
    price = models.FloatField(default=0)
    is_publish = models.BooleanField(default = False)
    is_deleted = models.CharField(max_length=1 , default='N')    #y=data deleted, N=data reserve
    active_objects = BookActiveManager()
    objects = models.Manager()
    inactive_objects = BookInactiveManager()

    class Meta:
        db_table = "bookinfo"
    
    def __str__(self):
        return self.name