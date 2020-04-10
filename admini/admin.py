from django.contrib import admin
from .models import AminModel,Company
# Register your models here.


# use of decorator
# @admin.register(Company)

# class ADNote(admin.StackedInline):
#     model = Note
#     extra = 1
#     max_num = 4

class CreateAdmin(admin.ModelAdmin):
    # inlines = [ADNote]
    list_display = ('name', 'company','jobs')
    # list_display = ('name','company_and_jobs' )
    # list_display_links = ( 'company','jobs')
    # list_editable =  ('name',)
    list_filter =  ['company',]
    search_fields = ['name','jobs']
    fields = [
        'name',
        'company',
        'jobs'
    ]
    # fieldsets = (
    #     (None,{
    #         'fields':(
    #             'name',
    #             'company',
    #             'jobs'
    #         )
    #     }),
    # )
# any field u ommit will be omiitted in the admin view of the particular model
    # def company_and_jobs(self, object):
    #     return "{} - {}".format(object.company, object.jobs)


# reister command which is better for me
admin.site.register(AminModel,CreateAdmin)
admin.site.register(Company)
# admin.site.register(Note)
