from django.db import models
from django.utils.text import slugify

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=50, 
        default="fas fa-cogs",
        help_text="FontAwesome icon class (e.g., fas fa-desktop)"
    )
    description = models.TextField(blank=True)
    sort_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Service Categories"
        ordering = ['sort_order', 'name']
    
    def __str__(self):
        return self.name

class Service(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('digital', 'Digital Engineering'),
        ('electrical', 'Electrical Designs'),
        ('programming', 'Industrial Programming'),
        ('consulting', 'Consulting'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
    icon = models.CharField(
        max_length=50, 
        blank=True,
        default="fas fa-cog",
        help_text="FontAwesome icon class"
    )
    summary = models.TextField(help_text="Short description for cards")
    full_description = models.TextField(help_text="Detailed description")
    
    # For progress bars
    show_progress_bars = models.BooleanField(default=False)
    
    sort_order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['sort_order', 'title']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
    text = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, default="fas fa-check-circle")
    sort_order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['sort_order']
    
    def __str__(self):
        return f"{self.service.title} - {self.text[:50]}"