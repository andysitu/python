from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime
from proj.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

def hello(request):
   return HttpResponse("Hello world")

def test(request):
   return HttpResponse("Hello")

# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse

def current_datetime(request):
   now = datetime.datetime.now()
   # t = get_template('current_datetime.html')
   # html = t.render(Context({'current_date': now}))
   # return HttpResponse(html)
   return render(request, 'dateapp/current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
   try:
      offset = int(offset)
   except ValueError:
      raise Http404()
   dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
   html = "In %s hour(s), it will be %s." % (offset, dt)
   # return HttpResponse(html)
   return render(request, 'dateapp/hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def display_meta(request):
   values = request.META.items()
   # values.sort()
   html = []
   for k, v in values:
      html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
   return HttpResponse('<table>%s</table>' % '\n'.join(html))

def contact(request):
   if request.method == 'POST':
      form = ContactForm(request.POST)
      if form.is_valid():
         cd = form.cleaned_data
         send_mail(
            cd['subject'],
            cd['message'],
            cd.get('email', 'noreply@example.com'),
            ['siteowner@example.com'],
         )
         return HttpResponseRedirect('/contact/thanks/')
   else:
      form = ContactForm(
         initial={'message': 'Please give input here.'}
         )
   return render(request, 'contact_form.html', {'form': form})