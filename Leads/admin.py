# ------------------------All-Import-------------------------
from django.contrib import admin
from django.conf.urls import url, include
from .models import NewApplicants,Lead_Category,Leads,Send_To,Status

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from import_export.admin import ImportExportModelAdmin

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail

import django.forms as forms
from django.core.mail import EmailMessage
from django.db.models import fields

from django.urls import include, path
import csv
from django.utils.html import format_html

from import_export.admin import ImportMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.admin import SimpleListFilter
from import_export.widgets import ForeignKeyWidget
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse

from import_export.formats import base_formats
from import_export.admin import ImportExportActionModelAdmin
 

from django.contrib import messages
from django.contrib.admin import helpers
from django.contrib.admin.utils import model_ngettext
from django.core.exceptions import PermissionDenied
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _, gettext_lazy

# -----------------------------Header-----------------

admin.site.site_title = 'nerdgeeklabsite'

admin.site.site_header ='Nerd-Geek-Lab'

admin.site.index_title = 'Admin Actions'




  # -----------------------NewApplicant admin------------
class NewApplicantsAdmin(ImportExportModelAdmin,ImportMixin):


    # --------------Delete Button------------------------
    def Edit(self, obj):
        return format_html(
            '<a class="btn" href="/admin/Leads/newapplicants/{}/change/"  style="width:100px;height:20px;color:white;background-color:green;border:1px solid black;border-radius:5px;">&nbsp &nbsp Edit &nbsp &nbsp</a>',
             obj.id)
    def Delete(self, obj):
        return format_html(

             '<a class="btn" href="/admin/Leads/newapplicants/{}/delete/" style="width:100px;height:20px;color:white;background-color:darkred;border:1px solid black;border-radius:5px;">&nbsp &nbsp Delete &nbsp &nbsp </a>',
             obj.id)
    Delete.allow_tags = True
    Delete.short_description = 'Delete'


# ----------------------lead Category obj------------------
    def lead_Category(obj):
        return ("%s " % (obj.name)).upper()
    lead_Category.short_description = 'name'

    def leads(obj):
        return ("%s " % (obj.name)).upper()
    leads.short_description = 'name'

# -----------------------Filtrers/Search----------------------
    search_fields = ('lead_Category__name','leads__name')
    list_filter = ('lead_Category','leads','Send_to','status')
   

# -----------------------_Change-template----------------
    change_form_template = 'admin/cutom.html'
    import_template_name = 'admin/import.html'
    actions_template = 'admin/changeit.html'

# ------0-------------------Other Field----------------------
    fields = ['lead_Category','email','name','leads','Send_to','status']
    lead_Category = None
    initial_readonly_fields = []
    list_display=['id','name','email','Field','Category','Send_to','status', 'Edit', 'Delete']
    list_display_links = ('name','id')
    initial_fields = ['lead_Category']

# ----------------get_fields/readonly/add_view/save---------

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj is None:
            fields = self.initial_fields
        return fields
    def get_readonly_fields(self, request, obj=None):
       
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj is None:
            readonly_fields = self.initial_readonly_fields
        return readonly_fields

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = dict(show_save=False)
        return super().add_view(request, form_url, extra_context)
   
        return super().changeform_view(request, object_id, extra_context=extra_context)
    def save_model(self, request, obj, form, change):
        self.lead_Category = obj.lead_Category


      
        return super().save_model(request, obj, form, change)

# --------------------------Dropdown Queryset------------------      
    def get_field_queryset(self, db, db_field, request):
        queryset = super().get_field_queryset(db, db_field, request)
        querysets = super().get_field_queryset(db, db_field, request)


        if db_field.name == 'leads':
            if queryset is None:
             
                queryset = Leads.objects.all()
            queryset = queryset.filter(lead_Category=self.lead_Category)


        
        if db_field.name == 'Send_to':
            if querysets is None:
                querysets = Send_To.objects.all()


            querysets = querysets.filter(lead_Category=self.lead_Category)

            return querysets

        return queryset           





# -----------------------------------------Urls-----------------  
    def get_urls(self):
        urls = super().get_urls()
        info = self.get_model_info()
        my_urls = [
            url(
                '_anotherbutton',
                self.admin_site.admin_view(self._anotherbutton),
                name='_anotherbutton',
            ),
            url(
                'excel',
                self.excel,
                name='excel',
            ),
          
        
  
        ]
        return my_urls + urls   

    
# ---------------------import_from_excel---------------
    def excel(self,request):
        return render(request,"admin/cutom.html")




# ---------------------------import Form-----------------
    def _anotherbutton(self, request):
        return render(request,"admin/import.html")


# -------------------------import formats----------

    def get_import_formats(self):
        
            formats = (
                
                  base_formats.XLSX,
        
            )
            return [f for f in formats if f().can_import()]
  

  # ----------------------------Email------------------
    actions = ['Email','delete_selected']


    def Email(modeladmin,request,queryset):
        opts = modeladmin.model._meta
        app_label = opts.app_label
        if request.POST.get('apply'):
            select=request.POST.get('select')

            if select=="Confirmation":
                msg_html = render_to_string('admin/msg1.html', {'orders': queryset})
                sub_html = render_to_string('admin/sub1.html', {'orders': queryset})
            else:
                msg_html = render_to_string('admin/msg2.html', {'orders': queryset})
                sub_html = render_to_string('admin/sub2.html', {'orders': queryset})

            for i in queryset:

                msg_html = msg_html
                sub_html = sub_html

                Subject=sub_html
                html_message=msg_html

                from_email=settings.EMAIL_HOST_USER
                if i.email:
                    send_mail(Subject,html_message, from_email,[i.email], fail_silently=False)

                    modeladmin.message_user(request,
                                      "Email Sent To {} orders".format(queryset.count()))
                    return HttpResponseRedirect(request.get_full_path())
        objects_name = model_ngettext(queryset)

   
        context = {
            **modeladmin.admin_site.each_context(request),
        
            'objects_name': str(objects_name),
            'queryset': queryset,
            'opts': opts,
            'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
            'media': modeladmin.media,
        }
        request.current_app = modeladmin.admin_site.name
        return TemplateResponse(request, [
            "admin/%s/%s/Email_Confirm.html" % (app_label, opts.model_name),
            "admin/%s/Email_Confirm" % app_label,
            "admin/Email_Confirm.html"
        ], context)


        


    Email.short_description = "Send Email"
#     def delete_selected(modeladmin, request, queryset):
#         """
#         Default action which deletes the selected objects.
#         This action first displays a confirmation page which shows all the
#         deletable objects, or, if the user has no permission one of the related
#         childs (foreignkeys), a "permission denied" message.
#         Next, it deletes all selected objects and redirects back to the change list.
#         """
        

#         # Populate deletable_objects, a data structure of all related objects that
#         # will also be deleted.
#         deletable_objects, model_count, perms_needed, protected = modeladmin.get_deleted_objects(queryset, request)

#         # The user has already confirmed the deletion.
#         # Do the deletion and return None to display the change list view again.
#         if request.POST.get('post') and not protected:
#             if perms_needed:
#                 raise PermissionDenied
#             n = queryset.count()
#             if n:
#                 for obj in queryset:
#                     obj_display = str(obj)
#                     modeladmin.log_deletion(request, obj, obj_display)
#                 modeladmin.delete_queryset(request, queryset)
#                 modeladmin.message_user(request, _("Successfully deleted %(count)d %(items)s.") % {
#                     "count": n, "items": model_ngettext(modeladmin.opts, n)
#                 }, messages.SUCCESS)
#             # Return None to display the change list page again.
#             return None

#         objects_name = model_ngettext(queryset)

#         if perms_needed or protected:
#             title = _("Cannot delete %(name)s") % {"name": objects_name}
#         else:
#             title = _("Are you sure?")

#         context = {
#             **modeladmin.admin_site.each_context(request),
#             'title': title,
#             'objects_name': str(objects_name),
#             'deletable_objects': [deletable_objects],
#             'model_count': dict(model_count).items(),
#             'queryset': queryset,
#             'perms_lacking': perms_needed,
#             'protected': protected,
#             'opts': opts,
#             'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
#             'media': modeladmin.media,
#         }

#         request.current_app = modeladmin.admin_site.name

#         # Display the confirmation page
#         return TemplateResponse(request, modeladmin.delete_selected_confirmation_template or [
#             "admin/%s/%s/delete_selected_confirmation.html" % (app_label, opts.model_name),
#             "admin/%s/delete_selected_confirmation.html" % app_label,
#             "admin/delete_selected_confirmation.html"
#         ], context)


#     delete_selected.allowed_permissions = ('delete',)
#     delete_selected.short_description = gettext_lazy("Delete %(verbose_name_plural)s")
# # -------------------------registration---------------------  

admin.site.register(NewApplicants,NewApplicantsAdmin)
admin.site.register(Status)
admin.site.register(Lead_Category)
admin.site.register(Leads)
admin.site.register(Send_To)

admin.site.unregister(User)
admin.site.unregister(Group)







































  # ---------------------------Filter----------------  
# class CountryFilter(SimpleListFilter):
#     title = 'Category' # or use _('country') for translated title
#     parameter_name = 'lead_Category'
    

#     def lookups(self, request, model_admin):
#         lead_Categorys = set([c.lead_Category for c in model_admin.model.objects.all()])
#         return [(c.id, c.name) for c in lead_Categorys]
#         # You can also use hardcoded model name like "Country" instead of 
#         # "model_admin.model" if this is not direct foreign key filter

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(lead_Category__id__exact=self.value())
#         else:
#             return queryset
    

# # ----------------------------------Adress Admin--------------------




# class AddressAdmin(ImportExportModelAdmin):
    

#   # --------------------------------Field--------------------
#     list_display=['id','name','leads','lead_Category','Send_to','status']
#     def lead_Category(obj):
#         return ("%s " % (obj.name)).upper()
#     lead_Category.short_description = 'name'
#     # change_list_template = "admin/heroes_changelist.html"


    
#     list_filter = (CountryFilter,)
#     # list_filter = (leadFilter,)

#     change_form_template = 'admin/cutom.html'
#     fields = ['lead_Category','leads','Send_to']
#     readonly_fields = ['lead_Category']

#     search_fields = ('lead_Category__name','leads__name')
#     # custom attributes (used in "add" view)
#     initial_fields = ['lead_Category']
#     initial_readonly_fields = []
#     lead_Category = None
   



# # ---------------------------Dropdowb----------------------
  
#     def get_fields(self, request, obj=None):
#         """ show initial fields in add view, show all fields in change view """
#         fields = super().get_fields(request, obj)
#         if obj is None:
#             fields = self.initial_fields
#         return fields

#     def get_readonly_fields(self, request, obj=None):
#         """ set the initial field readonly in the change view """
#         readonly_fields = super().get_readonly_fields(request, obj)
#         if obj is None:
#             readonly_fields = self.initial_readonly_fields
#         return readonly_fields

#     def add_view(self, request, form_url='', extra_context=None):
#         """ remove the save button from the "add" view """
#         extra_context = dict(show_save=False)
#         return super().add_view(request, form_url, extra_context)
   
#         return super().changeform_view(request, object_id, extra_context=extra_context)
#     def save_model(self, request, obj, form, change):
#         """ store the select country for use in get_field_queryset """
#         self.lead_Category = obj.lead_Category


      
#         return super().save_model(request, obj, form, change)
    # actions = ['update_status']

    # def update_status(self, request, queryset):
    #     # All requests here will actually be of type POST 
    #     # so we will need to check for our special key 'apply' 
    #     # rather than the actual request type
    #     if 'apply' in request.POST:
    #         # The user clicked submit on the intermediate form.
    #         # Perform our update action:
    #         queryset.update(status=1)
            
    #         # Redirect to our admin view after our update has 
    #         # completed with a nice little info message saying 
    #         # our models have been updated:
    #         self.message_user(request,
    #                           "Changed status on {} orders".format(queryset.count()))
    #         return HttpResponseRedirect(request.get_full_path())
                        
    #     return render(request,
    #                   'admin/custom_change_form.html',
    #                   context={'orders':queryset})

    # update_status.short_description = "Update status"





#     def get_field_queryset(self, db, db_field, request):

#         queryset = super().get_field_queryset(db, db_field, request)
#         querysets = super().get_field_queryset(db, db_field, request)


#         if db_field.name == 'leads':
#             if queryset is None:
             
#                 queryset = Leads.objects.all()
#             # Filter by country
#             queryset = queryset.filter(lead_Category=self.lead_Category)


        
#         if db_field.name == 'Send_to':
#             if querysets is None:
#                 querysets = Send_To.objects.all()


#             querysets = querysets.filter(lead_Category=self.lead_Category)

#             return querysets

#         return queryset           
    
  
       




