from django.views import View
from django.shortcuts import render
from .models import Product, Counter
from .forms import ContactForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import get_template
from .tasks import send_email_message
from django.db.models import F
from django.http import HttpResponseRedirect
import time
from django.http import JsonResponse
from django.template.loader import render_to_string


class IndexView(View):
    queryset = Product.objects.all()

    def get(self, request):
        return render(request, template_name='index.html', context={'products': self.queryset})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            current_site = get_current_site(request)
            site_name = current_site.name
            protocol = request.scheme
            domain = current_site.domain
            context = {
                'protocol': protocol, 'domain': domain,
                'email': form.cleaned_data['email'],
                'tel': form.cleaned_data['phone_number'],
                'name': form.cleaned_data['name']
            }
            message = get_template('coreapp/email_manager.html'). \
                render(context)
            Counter.objects.filter(name='entry').update(num_of_entries=F('num_of_entries') + 1)
            count = Counter.objects.only('num_of_entries')[0]
            subject = f'Заявка № {count.num_of_entries} на покупку товара на {site_name}'
            send_email_message(message, subject)
            time.sleep(1)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
