from django.contrib import admin
from .models import ServiceCategory, Service, ServiceFeature

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'service_type', 'category', 'sort_order', 'is_active']
    list_filter = ['service_type', 'category', 'is_active', 'is_featured']
    search_fields = ['title', 'summary']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'service_type', 'category', 'icon')
        }),
        ('Content', {
            'fields': ('summary', 'full_description')
        }),
        ('Display Options', {
            'fields': ('show_progress_bars', 'sort_order', 'is_featured', 'is_active')
        }),
    )

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'sort_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
    fields = ['name', 'icon', 'description', 'sort_order', 'is_active']