import queue


from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from apps.gugols.models import Publication, Category, OurWork, SendUserAdmin, Workers, Services, SignIn
from django.views import generic

from apps.gugols.forms import UserSendForm, SignInForm
from django.views.generic import FormView, ListView, CreateView


class BeautyListView(generic.ListView):
    template_name = 'blog.html'
    context_object_name = 'publications'

    def get_queryset(self):
        query_params = self.request.GET
        search_word = query_params.get('search_words')
        publication_qs = Publication.objects.all()
        if search_word:
            publication_qs = publication_qs.filter(name__contains=search_word)
        return publication_qs


class BeautyDetailView(generic.DetailView):
    template_name = 'blog-single.html'
    context_object_name = 'works'
    model = Workers
    slug_field = 'id'
    slug_url_kwarg = 'pub_pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeautyDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class BeautyIndexView(CreateView):
    template_name = 'index.html'
    form_class = SignInForm
    context_object_name = 'publications'
    model = SignIn
    success_url = "/publication/"

    def form_valid(self, form):
        self.form_class(form.cleaned_data)
        return super(BeautyIndexView, self).form_valid(form)


class BeautyAboutView(CreateView):
    template_name = 'about.html'
    form_class = SignInForm
    success_url = "/about/"
    model = SignIn

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeautyAboutView, self).get_context_data(**kwargs)
        context['about_list'] = Workers.objects.all()
        return context

    def form_valid(self, form):
        self.form_class(form.cleaned_data)
        return super(BeautyAboutView, self).form_valid(form)


class BeautyServiceView(CreateView):
    template_name = 'services.html'
    form_class = SignInForm
    success_url = "/service/"
    model = SignIn

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeautyServiceView, self).get_context_data(**kwargs)
        context['service'] = Services.objects.all()
        return context

    def form_valid(self, form):
        self.form_class(form.cleaned_data)
        return super(BeautyServiceView, self).form_valid(form)


class BeautyWorkView(CreateView, ListView):
    template_name = 'work.html'
    paginate_by = 9
    model = SignIn
    form_class = SignInForm
    success_url = "/work/"
    queryset = OurWork.objects.all()
    context_object_name = "works"

    def form_valid(self, form):
        self.form_class(form.cleaned_data)
        return super(BeautyWorkView, self).form_valid(form)

    def get_queryset(self):
        query_params = self.request.GET
        search_word = query_params.get('search_words')
        publication_qs = OurWork.objects.all()
        if search_word:
            publication_qs = publication_qs.filter(name__contains=search_word)
        return publication_qs


class BeautyContactView(CreateView):
    template_name = 'contact.html'
    form_class = SignInForm
    model = SignIn
    success_url = "/contact/"
    context_object_name = 'publications'

    def form_valid(self, form):
        self.form_class(form.cleaned_data)
        return super(BeautyContactView, self).form_valid(form)


def send_to_admin(request):
    if request.method == 'POST':
        post_request = request.POST
        email_form = UserSendForm(post_request)
        if email_form.is_valid():
            admin = SendUserAdmin.objects.create(
                name=email_form.data['name'],
                email=email_form.data['email'],
                message=email_form.data['message']
                )
            return redirect('contact-url')
        else:
            return HttpResponse(content=f'Похоже вы неправильно заполнили форму: {email_form.errors}')
