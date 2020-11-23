from django.conf.urls import include
from django.conf import settings
from django.urls import path,re_path
from django.contrib.auth import logout
from django.conf.urls.static import static
from . import views as core_views


# from . import views as core_views
# from django.contrib.auth import logout
from . import views

urlpatterns=[
    # path(r'',views.index,name = 'index_page'),
    re_path(r'index/(\d+)/$', views.index, name = 'index_page'),
    re_path(r'^new/p_unit$',views.p_unit,name='p_unit_form'),
    re_path(r'^new/state$',views.state,name='state_form'),
    re_path(r'^new/ward$',views.ward,name='ward_form'),
    re_path(r'^new/lga$',views.lga,name='lga_form'),
    re_path(r'^signup/$', core_views.signup_view, name='signup'),
    re_path(r'^sign-out/$', logout, name='logout'),
    re_path(r'^lga/(\w{2,})/$',views.lga_filter,name = 'lga'), 
    re_path(r'^polls/(\w+)/$',views.polls,name = 'polls'),


    # url(r'^single_listing/(\d+)/$',views.single_listing,name='single_listing'),
    # url(r'^new/listing$',views.listing,name='listing_form'),
    # url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^booking/(\d+)/$', views.booking, name='booking'),
    # url(r'^profile/(?P<username>[0-9]+)$',views.profile, name='profile'),
    # url(r'^new/image$',views.new_image,name='new_image'),
    # url(r'^listing/times(\d+)/$',views.listing_times,name='listing_times'),
    # url(r'^sign-out/$', logout, name='logout'),
   
    
    
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)