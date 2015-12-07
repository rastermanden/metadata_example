# -*- coding: utf-8 -*-
from django.contrib import admin
from metadata.models import Metadata

from django.http import HttpResponseRedirect

class MetadataAdmin(admin.ModelAdmin):
    def response_change(self, request, obj):
        return HttpResponseRedirect("/")
    ## redirect til frontpage efter add
    def response_add(self, request, obj):
        return HttpResponseRedirect("/")

    fieldsets = [
        ('Navnet metadatsættet', {'fields': ['title']}),
        ('Kaldenavn ', {'fields': ['slug']}),
        ('Resumé af metadatasættet ', {'fields': ['abstract']}),
        ('Formål ', {'fields': ['purpose']}),
        ('Kontaktinformation ', {'classes':
                                  ('collapse',),
                                  'fields': ['responsibleparty_organisationname','electronicmailaddress',('responsibleparty_individualname', 'responsibleparty_positionname','contactinfo_telephone','address_deliverypoint')]}),
                 
        ('Tid ', {'classes': ('collapse',),'fields': [('created','updated', 'beginposition','endposition')]}),
        ('søgestreng ', {'classes': ('collapse',),'fields': ['search_string']}),

    ]
    list_display = ('title', 'purpose')
    prepopulated_fields = {'search_string': ('title','abstract',), 'slug':('title',),}
    search_fields = ['title', 'abstract','purpose']
    

admin.site.register(Metadata, MetadataAdmin)

