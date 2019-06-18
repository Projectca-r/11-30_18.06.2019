from django.urls import path
from .views import *

urlpatterns = [
    path('', catalog_list, name='catalog_list_url'),
    path('catalog/<str:slug>/', CatalogDetail.as_view(), name='catalog_detail_url'),
# ==================================================================================
    # ---------------------------------------------------------------------------
# ================================ Category ==========================================
    path('category_tv/', category_tvs_list, name='category_tv_list_url'),
    path('category_tv/<str:slug>/', Category_TVDetail.as_view(), name='category_tv_detail_url'),
# --------------------------------------------------------------------------
    path('category_phone/', category_phones_list, name='category_phone_list_url'),
    path('category_phone/<str:slug>/', Category_PhoneDetail.as_view() , name='category_phone_detail_url'),
# --------------------------------------------------------------------------
    path('category_a_laptop/', category_a_laptops_list, name='category_a_laptop_list_url'),
    path('category_a_laptop/<str:slug>/', Category_a_laptopDetail.as_view(), name='category_a_laptop_detail_url'),
# ================================= Product =========================================
    path('product_tv/', product_tvs_list, name='product_tv_list_url'),
    path('product_tv/<str:slug>/', Product_TVDetail, name='product_tv_detail_url'),
# -----------------------------------------------------------------------------------
    path('product_phone/', product_phones_list, name='product_phone_list_url'),
    path('product_phone/<str:slug>/', Product_PhoneDetail, name='product_phone_detail_url'),
# -----------------------------------------------------------------------------------
    path('product_a_laptop/', product_a_laptops_list, name='product_a_laptop_list_url'),
    path('product_a_laptop/<str:slug>/', Product_a_laptopDetail, name='product_a_laptop_detail_url'),
# =================================== Cart =============================================
    path('orderitem/', orderitem_list, name='orderitem_list_url'),

# ================================= TV =========================================
    # path('lg/', lgs_list, name='lg_list_url'),
    # path('lg/<str:slug>/', lg_detail, name='lg_detail_url'),
# ---------------------------------------------------------------------------
    # path('samsung_tv/', samsung_tvs_list, name='samsung_tv_list_url'),
    # path('samsung_tv/<str:slug>/', samsung_tv_detail, name='samsung_tv_detail_url'),
# ---------------------------------------------------------------------------
    # path('sony/', sonys_list, name='sony_list_url'),
    # path('sony/<str:slug>/', sony_detail, name='sony_detail_url'),
# ---------------------------------------------------------------------------
    # path('panasonic/', panasonics_list, name='panasonic_list_url'),
    # path('panasonic/<str:slug>/', panasonic_detail, name='panasonic_detail_url'),
# =================================== phone ==================================
    # path('samsung/', samsungs_list, name='samsung_list_url'),
    # path('samsung/<str:slug>/', samsung_detail, name='samsung_detail_url'),
# ----------------------------------------------------------------------------
    # path('apple/', apples_list, name='apple_list_url'),
    # path('apple/<str:slug>/', apple_detail, name='apple_detail_url'),
# ---------------------------------------------------------------------------
    # path('xiaomi/', xiaomis_list, name='xiaomi_list_url'),
    # path('xiaomi/<str:slug>/', xiaomi_detail, name='xiaomi_detail_url'),
# =================================== a_laptop=================================
    # path('mac_os/', mac_oss_list, name='mac_os_list_url'),
    # path('mac_os/<str:slug>/', mac_os_detail, name='mac_os_detail_url'),
# -----------------------------------------------------------------------------
    # path('asus/', asuss_list, name='asus_list_url'),
    # path('asus/<str:slug>/', asus_detail, name='asus_detail_url'),
# -----------------------------------------------------------------------------
    # path('acer/', acers_list, name='acer_list_url'),
    # path('acer/<str:slug>/', acer_detail, name='acer_detail_url'),
# =============================================================================
    # path('categorys/tvs/', tvs_list, name='tvs_list_url'),
    # path('categorys/tvs/<str:slug>/', tvs_detail, name='tvs_detail_url'),
    # path('categorys/phones/', phones_list, name='phones_list_url'),
    # path('categorys/a_laptops/', a_laptops_list, name='a_laptops_list_url'),
]