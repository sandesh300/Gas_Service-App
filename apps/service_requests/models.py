from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Service Categories"
    
    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    )
    
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='service_requests')
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    assigned_staff = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_requests'
    )
    location = models.CharField(max_length=255)
    preferred_date = models.DateField(null=True, blank=True)
    preferred_time = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.customer.email}"

class ServiceRequestAttachment(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f"Attachment for {self.service_request.title}"

class ServiceRequestComment(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Comment by {self.user.email} on {self.service_request.title}"

from django.db import migrations

def create_default_categories(apps, schema_editor):
    ServiceCategory = apps.get_model('service_requests', 'ServiceCategory')
    categories = [
        {
            'name': 'Gas Leak',
            'description': 'Emergency service for gas leaks and related safety concerns',
            'is_active': True
        },
        {
            'name': 'Installation',
            'description': 'New gas line installation or appliance hookup',
            'is_active': True
        },
        {
            'name': 'Maintenance',
            'description': 'Regular maintenance and inspection services',
            'is_active': True
        },
        {
            'name': 'Meter Issues',
            'description': 'Problems with gas meter reading or functionality',
            'is_active': True
        },
        {
            'name': 'Billing Query',
            'description': 'Questions or concerns about billing',
            'is_active': True
        }
    ]
    
    for category in categories:
        ServiceCategory.objects.create(**category)

def reverse_categories(apps, schema_editor):
    ServiceCategory = apps.get_model('service_requests', 'ServiceCategory')
    ServiceCategory.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('service_requests', '0001_initial'),  # Update this to your last migration
    ]

    operations = [
        migrations.RunPython(create_default_categories, reverse_categories),
    ]