from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .forms import ContactUsForm, ArticleForm


def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, "acceuil.html", context)


def apropos(request):
    return render(request, "article/apropos.html")


def contact(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["nom"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request, 'article/contact.html', {'form': form})


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'article/article_detail.html', {'article': article})

@login_required
def article_create(request): 
    if request.method == 'POST': 
        form = ArticleForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save()
            return HttpResponseRedirect('/')
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ArticleForm()

    return render(request, 'article/articleForm.html', {'form': form})

def article_update(request, id):
    article = Article.objects.get(id=id)

    if request.method == 'POST':
        form = ArticleForm(request.POST,  request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request,
                  'article/article_update.html',
                  {'form': form})

def article_delete(request, id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        article.delete()
        return redirect('/')
    else:
        return render(request, "article/article_delete.html", {"article": article})
