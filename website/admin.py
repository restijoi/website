from django.contrib import admin

from website.models import Project, Team
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','slug','description','created','rating_likes','public_views','private_views','funding','goal','paypal','created','modified')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('project','user','role','created','modified')


admin.site.unregister(User)
UserAdmin.list_display = ('id','username','email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff')


admin.site.register(User, UserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Team, TeamAdmin)
