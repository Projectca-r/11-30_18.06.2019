from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.shortcuts import reverse

# Create your models here.

def media(instance, filename):
    image = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, image)

class Catalog(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(db_index=True, upload_to=media)

    def get_absolute_url(self):
        return reverse('catalog_detail_url', kwargs={'slug': self.slug})
	# TV
	# a_laptop
	# Phone


    def __str__(self):
        return self.title

# ======================================================================================
# Category

class Category_TV(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='tv_catalog')

    def get_absolute_url(self):
        return reverse('category_tv_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug

# ------------------------------------------------------------------------------

class Category_Phone(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='phone_catalog')

    def get_absolute_url(self):
        return reverse('category_phone_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug

# -------------------------------------------------------------------------------

class Category_a_laptop(models.Model):
    catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='a_laptop_catalog')

    def get_absolute_url(self):
        return reverse('category_a_laptop_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug

# ==============================================================================
# ==============================================================================
# ==============================================================================
# TV

class Product_TV(models.Model):
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='catalog_tv')
    category_tv = models.ManyToManyField('Category_TV', blank=True, related_name='tv')    
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=30, db_index=True)
    screen = models.CharField(max_length=30, db_index=True) # Ultra HD 4K (3840x2160 пикселей)
    connect = models.CharField(max_length=30, db_index=True) # Wi-fi
    size = models.CharField(max_length=30, db_index=True) #77 дюймов (195 см)    
    # text = models.TextField(blank=True, db_index=True)
    decimal = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    

    def get_absolute_url(self):
        return reverse('tv_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title



# ==============================================================================

# ===================================================================================

# ===============================Phone===================================


class Product_Phone(models.Model):
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='catalog_phone')
    category_phone = models.ManyToManyField('Category_Phone', blank=True, related_name='phone')    
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=30, db_index=True)
    camera = models.CharField(max_length=30, db_index=True) # 16px
    memory = models.CharField(max_length=30, db_index=True) # 16gb
    connect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    decimal = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    

    def get_absolute_url(self):
        return reverse('phone_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
# ======================================================================

# ============================ a laptop ================================


class Product_a_laptop(models.Model):
    catalog = models.ManyToManyField('Catalog', blank=True, related_name='catalog_a_laptop')
    category_a_laptop = models.ManyToManyField('Category_a_laptop', blank=True, related_name='a_laptop')    
    image = models.ImageField(upload_to=media, db_index=True)
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=30, db_index=True)
    touch = models.CharField(max_length=30, db_index=True, blank=True) # Touch ID
    weight = models.CharField(max_length=30, db_index=True) # 1,25 кг
    memory = models.CharField(max_length=30, db_index=True) # 16gb
    onnect = models.CharField(max_length=30, db_index=True) # Wi-fi bluetooth
    thickness = models.CharField(max_length=30, db_index=True) # толщина 15,6 мм
    ssd = models.CharField(max_length=30, db_index=True) # SSD‑накопитель до 1,5 ТБ 
    decimal = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    

    def get_absolute_url(self):
        return reverse('a_laptop_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
# ======================================================================================
# ----------------------------------------
# class OrderItem(models.Model):
#     product_tv = models.OneToOneField(Product_TV, on_delete=models.SET_NULL, null=True, blank=True)
#     product_phone = models.OneToOneField(Product_Phone, on_delete=models.SET_NULL, null=True, blank=True)
#     product_a_laptop = models.OneToOneField(Product_a_laptop, on_delete=models.SET_NULL, null=True, blank=True)
#     slug = models.SlugField(blank=True)
#     is_ordered = models.BooleanField(default=False)
#     date_added = models.DateTimeField(auto_now=True)
#     date_ordered = models.DateTimeField(null=True)

#     def __str__(self):
#         return '{}'.format(self.product_tv, self.product_phone, self.product_a_laptop)


# class Order(models.Model):
#     ref_code = models.CharField(max_length=15)
#     # owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
#     is_ordered = models.BooleanField(default=False)
#     items = models.ManyToManyField(OrderItem)
#     date_ordered = models.DateTimeField(auto_now=True)

#     def get_cart_items(self):
#         return self.items.all()

#     def __str__(self):
#         return self.ref_code
        # return '{0} - {1}'.format(self.owner, self.ref_code)
# =====================================================================================

# =================================================================================





# class Product(models.Model): 
#     catalogs = models.ForeignKey(Catalog, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200, db_index=True)

# Category.objects.values()
# [{'id': 1, 'catalogs_id': 1, 'slug': 'LG'},
#  {'id': 2, 'catalogs_id': 1, 'slug': 'Samsung-TV'},
#  {'id': 3, 'catalogs_id': 1, 'slug': 'Sony'},
#  {'id': 4, 'catalogs_id': 1, 'slug': 'Panasonic'},
#  {'id': 5, 'catalogs_id': 2, 'slug': 'Samsung'},
#  {'id': 6, 'catalogs_id': 2, 'slug': 'Apple'},
#  {'id': 7, 'catalogs_id': 2, 'slug': 'Xiaomi'},
#  {'id': 8, 'catalogs_id': 3, 'slug': 'Apple_OS'},
#  {'id': 9, 'catalogs_id': 3, 'slug': 'ASUS'},
#  {'id': 10, 'catalogs_id': 3, 'slug': 'ACER'}]

# Create your models here.
