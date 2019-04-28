from django.contrib import admin
from django.contrib.contenttypes.models import ContentType


import nested_admin





# Register your models here.

from .models import *


class BrandModelServiceItemMapInline(nested_admin.NestedTabularInline):
    model = BrandModelServiceItemMap

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(BrandModelServiceItemMapInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'brand_model':
            # field.queryset = ContentType.objects.filter(model__icontains="brand", app_label="facts_and_features_management")
            field.queryset = ContentType.objects.filter(app_label="testapp")

        return field


class SymptomInline(nested_admin.NestedTabularInline):
    model = Symptom
    extra = 0
    exclude = ['service_item']

class SymptomInlineForServiceItem(nested_admin.NestedTabularInline):
    model = Symptom
    extra = 0
    exclude = ['category']

class ServiceItemInline(nested_admin.NestedTabularInline):
    model = ServiceItem
    extra = 0
    inlines = [SymptomInlineForServiceItem, BrandModelServiceItemMapInline]


class BrandModelCategoryMapInline(nested_admin.NestedTabularInline):
    model = BrandModelCategoryMap

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(BrandModelCategoryMapInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'brand_model':
            # field.queryset = ContentType.objects.filter(model__icontains="brand", app_label="facts_and_features_management")
            field.queryset = ContentType.objects.filter(app_label="testapp")

        return field




class CategoryAdmin(nested_admin.NestedModelAdmin):
    inlines = []

    class Media:
        css = {
             'all': ('css/admin/my_own_admin.css',)
        }

    def get_inlines(self, obj):
        if obj.map_to == 0:
            return [ServiceItemInline]
        elif obj.map_to == 1:
            return [BrandModelCategoryMapInline, SymptomInline]
        else:
            return [SymptomInline]
        # return [ServiceItemInline, BrandModelCategoryMapInline, SymptomInline]

    def get_form(self, request, obj=None, **kwargs):
        if (obj): self.inlines = self.get_inlines(obj)
        return super(CategoryAdmin, self).get_form(request, obj, **kwargs)


class testinline1(admin.TabularInline):
    model = Symptom

class testinline2(admin.TabularInline):
    model = BrandModelServiceItemMap

class ServiceItemAdmin(admin.ModelAdmin):
    inlines = [testinline1, testinline2]

    class Media:
        css = {
             'all': ('css/admin/my_own_admin.css',)
        }



admin.site.register(Category, CategoryAdmin)
# admin.site.register(ServiceItem, ServiceItemAdmin)
# admin.site.register(BrandModelCategoryMap)
# admin.site.register(Symptom)
