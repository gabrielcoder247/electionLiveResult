from django.contrib import admin

# Register your models here.


from django.contrib import admin
from bincom import models


# Register your models here.


from bincom.models import (AgentDetail, Announced_lga_result, Announced_pu_result,
Announced_state_result, Announced_ward_result, Lga, Party, Polling_unit, State, Ward)


admin.site.site_header="Election live Result"
admin.site.site_title="Admin"

@admin.register(models.AgentDetail)
class AgentDetailAdmin(admin.ModelAdmin):

    # date_hierarchy = 'created'
    # search_fields = ['title', 'location',]
    list_display = ('id','firstname','lastname','email','phone','address',)
    # list_filter = ('status',)


@admin.register(models.Announced_lga_result)
class Announced_lga_resultAdmin(admin.ModelAdmin):
    list_display = ('id','lga_name','party_abbreviation','party_score','date_entered','user_ip_address',)



@admin.register(models.Announced_pu_result)
class Announced_pu_resultAdmin(admin.ModelAdmin):
    list_display = ('id','lga_name','party_abbreviation','party_score','date_entered','user_ip_address',)


@admin.register(models.Announced_state_result)
class Announced_state_resultAdmin(admin.ModelAdmin):
    list_display = ('id','state_name','party_abbreviation','party_score','date_entered','user_ip_address')


@admin.register(models.Announced_ward_result)
class Announced_ward_resultAdmin(admin.ModelAdmin):
    list_display = ('id','ward_name','party_abbreviation','party_score','date_entered','user_ip_address')

@admin.register(models.Lga)
class LgaAdmin(admin.ModelAdmin):
    list_display = ('id','lga_name','lga_description','date_entered','user_ip_address')



@admin.register(models.Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('id','party_name')



@admin.register(models.Polling_unit)
class Polling_unitAdmin(admin.ModelAdmin):
    list_display = ('id','polling_unit_name','party_score','polling_unit_description','date_entered','lat','lng','user_ip_address')



@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('id','state_name')

@admin.register(models.Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('id','ward_name','polling_unit_name','ward_description','date_entered','user_ip_address')



