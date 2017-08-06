from django.contrib import admin

# Register your models here.
from api.models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('heading', 'body', 'publishedOn', 'publishedBy')
    list_filter = ('publishedOn', 'publishedBy')
    search_fields = ['heading', 'body']

class MemberAdmin(admin.ModelAdmin):
    fields = ('user', 'isApproved', 'mobile')
    list_display = ('__str__', 'isApproved', 'mobile')
    list_editable = ['isApproved', 'mobile']
    search_fields = ['user__first_name', 'user__last_name']

class SIGAdmin(admin.ModelAdmin):
    list_display = ('topic', 'date', 'fromTime', 'toTime')
    list_filter = ('date',)
    search_fields = ['topic', 'description']

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'fromDateTime', 'toDateTime', 'location')
    list_filter = ('fromDateTime',)
    search_fields = ['name', 'description']

class CouncilMemberAdmin(admin.ModelAdmin):
    list_display = ('member', 'designation')

admin.site.register(News, NewsAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(SIG, SIGAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(CouncilMember, CouncilMemberAdmin)
