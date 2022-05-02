
from django.contrib import admin

from apps.gugols.models import Category, Publication, OurWork, SendUserAdmin, Workers, Services, SignIn


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass


@admin.register(OurWork)
class OurWorkAdmin(admin.ModelAdmin):
    pass


@admin.register(SendUserAdmin)
class UserSendAdmin(admin.ModelAdmin):
    pass


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    pass


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    pass


@admin.register(SignIn)
class SignInAdmin(admin.ModelAdmin):
    pass
