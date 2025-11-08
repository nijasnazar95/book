from django.contrib import admin
from .models import Book
# Register your models here.




# class ModelAdminBook(admin.ModelAdmin):
#     list_display=['name','author','price','description']
#     list_filter=['name','author']
#     search_fields=['name','author']
#     list_editable=['price']

class ModelAdminBook(admin.ModelAdmin):
        list_display=['name','author','price','description']

        actions=['mark_free']

        def mark_free(self,request,queryset):
                queryset.update(price=0)
                self.message_user(request,"Books marked as free")
        mark_free.short_description = "marks selected books as free"



admin.site.register(Book ,ModelAdminBook)