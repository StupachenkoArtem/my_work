from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import LoginUserForm
from .models import *
from .utils import DataMixin

menu = [{'title': 'Галерея', 'url_name': 'gallery'},
        {'title': 'Коллекции', 'url_name': 'collections'},
        {'title': "MIKHAL'CHUK", 'url_name': "MIKHAL'CHUK"},
        {'title': 'Контакты', 'url_name': 'contact'}]


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'mikhalchuk/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return {**context, **c_def}


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'mikhalchuk/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def index(request):
    context = {
        'menu': menu,
        'title': "MIKHAL'CHUK"
    }

    return render(request, 'mikhalchuk/index.html', context=context)


class CollectionView(ListView):
    model = Collection
    template_name = 'mikhalchuk/collections.html'
    context_object_name = 'collections'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Collection'
        context['collections_with_photos'] = []
        for collection in context['collections']:
            photos = Photo.objects.filter(collection=collection)
            context['collections_with_photos'].append({
                'collection': collection,
                'photos': photos
            })
        return context


def photo_view(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    photos = collection.photo_set.all()
    return render(request, 'photo_collection.html', {'collection': collection, 'photos': photos})


def mikhalchuk(request):
    return HttpResponse("MIKHAL'CHUK")


def contact(request):
    context = {
        'menu': menu,
        'title': "CONTACTS"
    }
    return render(request, 'mikhalchuk/contacts.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Cтраница не найдена</h1>')


class NewCollectionView(ListView):
    model = NewCollection
    template_name = 'mikhalchuk/newcollection.html'
    context_object_name = 'newcollections'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'NewCollection'
        return context


class DressView(ListView):
    model = Dress
    template_name = 'mikhalchuk/dress.html'
    context_object_name = 'dress'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Dress'
        return context


class JacketsView(ListView):
    model = Jackets
    template_name = 'mikhalchuk/jackets.html'
    context_object_name = 'jackets'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Jackets'
        return context


class ShirtsAndBlousesView(ListView):
    model = ShirtsAndBlouses
    template_name = 'mikhalchuk/shirts_and_blouses.html'
    context_object_name = 'shirts_and_blouses'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'ShirtsAndBlouses'
        return context


class TrousersAndSkirtsView(ListView):
    model = TrousersAndSkirts
    template_name = 'mikhalchuk/trousers_and_skirts.html'
    context_object_name = 'trousers_and_skirts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'TrousersAndSkirts'
        return context

