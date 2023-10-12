from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Messages

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display Username field
    fields = ['username']
    inlines = [ProfileInline]

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Messages)