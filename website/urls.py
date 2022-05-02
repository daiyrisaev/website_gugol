"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.gugols.views import BeautyIndexView, BeautyListView, BeautyDetailView, BeautyAboutView, BeautyServiceView, \
    BeautyContactView, BeautyWorkView, send_to_admin

from apps.gugols import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publication/',BeautyIndexView.as_view(), name='publications_list-url'),
    path('public/',BeautyListView.as_view(), name='publication_list-url'),
    path('publications/<int:pk>/',BeautyDetailView.as_view(), name='publication_detail-url'),
    path('about/',BeautyAboutView.as_view(), name='about-url'),
    path('service/',BeautyServiceView.as_view(), name='service-url'),
    path('work/',BeautyWorkView.as_view(), name='work-url'),
    path('contact/',BeautyContactView.as_view(), name='contact-url'),
    path('email/',send_to_admin, name='email-url'),
    path('booking/',views.create_booking_tour, name='booking-url'),
    # path('blog/<int:pk>/comment-add/',add_comment_publication, name='add-publication-comment-url'),



]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)