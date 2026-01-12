from django.db import models
from django.conf import settings
from django.db.models import Q
User = settings.AUTH_USER_MODEL


class ProudctQuerySet(models.QuerySet):

    def is_public(self):
        return self.filter(public=True)

    def search(self, query, user=None):
        if not query:
            return self.none()  # avoid None error

        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        qs = self.filter(lookup)

        if user is not None:
            qs = qs.is_public().filter(user=user)

        return qs



class ProductManager(models.Manager):

    def get_queryset(self,*args, **kwargs):
        return ProudctQuerySet(self.model, using=self._db)


    def search(self, query,user=None):
        return self.get_queryset().search(query,user=user)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15,default=99.99)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)
    
    def get_discount(self):
        return "80% off"