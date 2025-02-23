from django.contrib import admin
from .models import ServiceCategory, ServiceRequest, ServiceRequestAttachment, ServiceRequestComment

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    search_fields = ('name',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'customer', 'category', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('title', 'description', 'customer__email')
    raw_id_fields = ('customer', 'assigned_staff')
    date_hierarchy = 'created_at'

@admin.register(ServiceRequestAttachment)
class ServiceRequestAttachmentAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'uploaded_at', 'description')
    search_fields = ('service_request__title', 'description')

@admin.register(ServiceRequestComment)
class ServiceRequestCommentAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'user', 'created_at')
    search_fields = ('service_request__title', 'user__email', 'comment')
