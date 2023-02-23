from django.contrib import admin

from products.admin import BasketAdmin
from users.models import EmailVerification, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailRegistrationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'created', 'expiration')
    fields = ('code', 'user', 'created', 'expiration')
    readonly_fields = ('created',)
