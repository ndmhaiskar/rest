from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import RestaurantLocation
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    """Update Restaurant Location"""

    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/detail-update.html'

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Update Restaurant: {name}'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    """Create form view"""

    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'forms.html'
    # template_name = 'restaurants/forms.html'
    # success_url = '/restaurants/'

    def form_valid(self, form):
        instance = form.save()
        instance.owner = self.request.user
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        """Get context data of restaurant item"""
        context = super(RestaurantCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context


@login_required()
def restaurant_createview(request):
    """Create a form element"""

    # form = RestaurantCreateForm(request.POST or None)
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        """obj = RestaurantLocation.objects.create(
            name=form.cleaned_data.get('name'),
            location=form.cleaned_data.get('location'),
            category=form.cleaned_data.get('category')
        )"""
        # form.save()
        # return HttpResponseRedirect('/restaurants/')
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            return HttpResponseRedirect('/restaurants/')
        else:
            return HttpResponseRedirect('/login/')

    if form.errors:
        errors = form.errors
    """template_name = 'restaurants/forms.html'
    context = {'form': form, 'errors': errors}
    return render(request, template_name, context)"""


def restaurant_detailview(request, slug):
    template_name = 'restaurants/restaurantlocation_detail.html'
    obj = RestaurantLocation.objects.get(slug=slug)
    context = {
        'object': obj
    }
    return render(request, template_name, context)


class RestaurantDetailView(LoginRequiredMixin, DetailView):
    """Detail class view for restaurant using rest_id"""

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
        # queryset = RestaurantLocation.objects.all()

    """def get_object(self, *args, **kwargs):
        rest_id = self.kwargs.get('rest_id')
        obj = get_object_or_404(RestaurantLocation, id=rest_id)
        return obj"""


class RestaurantListView(LoginRequiredMixin, ListView):
    """Class based List view of restaurants"""
    def get_queryset(self):
        """slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug)|
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset"""
        return RestaurantLocation.objects.filter(owner=self.request.user)


def restaurant_listview(request,):
    template_name = 'restaurants/restaurants_listview.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        rand_num = None
        some_list = [random.randint(1, 100000),
                     random.randint(1, 100000),
                     random.randint(1, 100000)
                     ]
        rand_num = random.randint(1, 1000000)
        bool_var = True
        if bool_var:
            rand_num = random.randint(1, 100000)
        context = {"some_list": some_list, "rand_num": rand_num}
        return context


def home(request):
    rand_num = None
    some_list = [random.randint(1, 100000),
                 random.randint(1, 100000),
                 random.randint(1, 100000)
                 ]
    rand_num = random.randint(1, 1000000)
    bool_var = True
    if bool_var:
        rand_num = random.randint(1, 100000)
    context = {"some_list": some_list, "rand_num": rand_num}
    return render(request, 'home.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'contact.html', context)


def contact(request):
    context = {}
    return render(request, 'contact.html', context)


def home_old(request):
    """ return HttpResponse('Hello World!')  How django works """
    # How django renders html
    rand_num = random.randint(1, 100000000)
    py_var = "python str"
    html_ = f"""<!DOCTYPE html>
    <html lang="eng">
        <head>
            <title>
                How html render
            </title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
        </head>
        <body>
            <p><h3>I am so good to go</h1></p>
            <p>
                <a href="http://www.google.com">
                    Link To Google
                </a>
                <p>Variable new as {py_var} and random number is { rand_num } </p>
            </p>
        </body>
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
    </html>
    """
    return HttpResponse(html_)
