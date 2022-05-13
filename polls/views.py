from django.shortcuts import render

# Create your views here.
from html.entities import name2codepoint
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
# from matplotlib.style import context
from django.urls import reverse
import sqlite3
from django.core.mail import send_mail
from .models import Poll, Choice, Teilnehmer




# erste seite auf meiner Webseite
def index(request):
    
    context = {'umfragen': Poll.objects.all(), 'title': "ESG Skills"}
    # print(context)
    return render(request=request, template_name='polls/index.html',
                context = context)

def umfrage_details(request,slug):
    
    if slug == 'anmelden':
        # return HttpResponse('Slug: {0}'.format(slug))
        # umfrage = Poll.objects.get(slug=slug)
        umfrage = get_object_or_404(Poll, slug=slug)#
        # print(umfrage) Thema_1 (Slug: Programmiersprache)
        
        context = {'umfrage': umfrage}
        # return HttpResponse(umfrage.name)
        return render(request=request, template_name='polls/umfrage.html',
                    context = context)
    elif slug == 'Idee':
        return render(request=request, template_name='polls/idee_reg.html')

        
def idee_reg(request):

    name = request.POST.get('name')
    email = request.POST.get('email')
    # a = Teilnehmer.objects.values
    print(email)
    send_mail(
    'Anmeldung',
    name + 'will sich anmelden seine Email_Adresse ist ' + email,
    # from
    'hassanalmuaz0@gmail.com',
    # to
    [email],
    )
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute(f"insert into polls_teilnehmer (name,email) values (?,?)", (name,email))
    conn.commit()
    context = {'name':name, 'email':email}
    return render(request=request, template_name='polls/idee_reg_danke.html', context=context)



    
def vote(request, slug):
    name = request.POST.get('name')
    email = request.POST.get('email')
    umfrage = get_object_or_404(Poll, slug=slug)
    ausgewahlte_antwort = umfrage.choice_set.get(pk=request.POST['choice']).name
    
    context = {'umfrage':umfrage, 'name':name, 'email':email, 'ausgewahlte_antwort':ausgewahlte_antwort}
    try:
        # post wird in umfrgae.html name = "choice" definiert und gibt mir eine dic  
        ausgewahlte_antwort = umfrage.choice_set.get(pk=request.POST['choice'])
        # print(ausgewahlte_antwort) 1,2 oder 3 id üz
    except (KeyError, Choice.DoesNotExist):
        return HttpResponse("Fehler: keine bzw. eine ungueltige Antwort ausgewaehlt!")
    else:
        ausgewahlte_antwort.votes += 1
        ausgewahlte_antwort.save()
        return render(request=request, template_name='polls/results.html', context=context)
        # return HttpResponseRedirect(reverse('results', args=(umfrage.slug,)))


def results(request, slug):
    # return HttpResponse('Slug: {0}'.format(slug))
    # umfrage = Poll.objects.get(slug=slug)
    name = request.GET.get('name')
    email = request.POST.get('email')
    print(name)
    umfrage = get_object_or_404(Poll, slug=slug)
    context = {'umfrage': umfrage, 'name':name, 'email':email}
    # return HttpResponse(umfrage.name)
    return render(request=request, template_name='polls/results.html',
                context = context)