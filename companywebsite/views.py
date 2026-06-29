from django.shortcuts import render
from .models import ServiceCategory, Service
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django.views.generic import TemplateView,FormView
from .forms import ContactForm
def services(request):
    # Get active categories
    categories = ServiceCategory.objects.filter(is_active=True).order_by('sort_order')
    bms_services = Service.objects.filter(
        category__name__icontains='BMS',
        is_active=True
    ).order_by('sort_order')
    
    # Get services by type
    service_types = {
        'digital': Service.objects.filter(service_type='digital', is_active=True).order_by('sort_order'),
        'electrical': Service.objects.filter(service_type='electrical', is_active=True).order_by('sort_order'),
        'programming': Service.objects.filter(service_type='programming', is_active=True).order_by('sort_order'),
        
    }
    
    context = {
        'categories': categories,
        'digital_services': service_types.get('digital', []),
        'electrical_services': service_types.get('electrical', []),
        'programming_services': service_types.get('programming', []),
        
    }
    
    return render(request, 'companywebsite/services.html', context)

# Keep other views the same
def home(request):
    return render(request, 'companywebsite/home.html')

def about(request):
    return render(request, 'companywebsite/about.html')

#def contact(request):
 #   return render(request, 'companywebsite/contact.html')

class SuccesView(TemplateView):
    template_name="companywebsite/success.html"

# views.py - update the form_valid method
class ContactView(FormView):
    form_class = ContactForm
    template_name = "companywebsite/contact.html"

    def get_success_url(self):
        return reverse("success")
    
    def form_valid(self, form):
        print("=" * 50)
        print("FORM IS VALID!")
        print("Form data:", form.cleaned_data)
        print("=" * 50)
        
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        phone = form.cleaned_data.get("phone", "Not provided")
        company = form.cleaned_data.get("company", "Not provided")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        
        full_message = f"""
        New Contact Form Submission:
        
        Name: {name}
        Email: {email}
        Phone: {phone}
        Company: {company}
        Subject: {subject}
        
        Message:
        {message}
        """
        
        print("Email content would be:")
        print(full_message)
        
        try:
            send_mail(
                subject=f"New Contact Form: {subject}",
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.NOTIFY_EMAIL],
                fail_silently=False,
            )
            print("✅ Email sent successfully!")
        except Exception as e:
            print(f"❌ Email sending failed: {e}")
        
        return super().form_valid(form)

