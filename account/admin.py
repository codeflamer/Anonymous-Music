from django.contrib import admin
from .models import UserProfile
# Register your models here.
class UserProfileModification(admin.ModelAdmin):
    list_display= ('user','user_info','city','website')

    def user_info(self,obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileModification,self).get_queryset(request)
        queryset = queryset.order_by('-city','user')

        return queryset
    user_info.short_description = 'Info'

admin.site.register(UserProfile,UserProfileModification)
# admin.site.site_header = 'Admin Codeflamer'