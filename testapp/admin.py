from django.contrib import admin
from django.contrib.contenttypes.models import ContentType




# Register your models here.

from .models import *

class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 1


class BrandModelCategoryMapInline(admin.TabularInline):
    model = BrandModelCategoryMap

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(BrandModelCategoryMapInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'brand_model':
            # field.queryset = ContentType.objects.filter(model__icontains="brand", app_label="facts_and_features_management")
            field.queryset = ContentType.objects.filter(app_label="testapp")

        return field


class BrandModelServiceItemMapInline(admin.TabularInline):
    model = BrandModelServiceItemMap

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):

        field = super(BrandModelServiceItemMapInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name == 'brand_model':
            # field.queryset = ContentType.objects.filter(model__icontains="brand", app_label="facts_and_features_management")
            field.queryset = ContentType.objects.filter(app_label="testapp")

        return field


class SymptomInline(admin.TabularInline):
    model = Symptom
    extra = 1
    exclude = ['service_item']

class SymptomInlineForServiceItem(admin.TabularInline):
    model = Symptom
    extra = 1
    exclude = ['category']


class CategoryAdmin(admin.ModelAdmin):
    inlines = []

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


class ServiceItemAdmin(admin.ModelAdmin):
    inlines = [SymptomInlineForServiceItem, BrandModelServiceItemMapInline]



admin.site.register(Category, CategoryAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
# admin.site.register(BrandModelCategoryMap)
# admin.site.register(Symptom)
