import queue

from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

from apps.gugols.models import Publication, Category, OurWork, SendUserAdmin, Workers, Services, SignIn
from django.views import generic

from apps.gugols.forms import UserSendForm, SignInForm


class BeautyListView(generic.ListView):
    template_name = 'blog.html'
    context_object_name = 'publications'

    def get_queryset(self):
        query_params = self.request.GET
        search_word = query_params.get('search_words')
        category_id = query_params.get('category_pk')
        publication_qs = Publication.objects.all()
        if search_word:
            publication_qs = publication_qs.filter(name__contains=search_word)
        if category_id:
            try:
                category_id = int(category_id)
            except ValueError:
                pass
            else:
                publication_qs = publication_qs.filter(category_id=category_id)
        return publication_qs


class BeautyDetailView(generic.DetailView):
    template_name = 'blog-single.html'
    context_object_name = 'publication'
    model = Publication
    slug_field = 'id'
    slug_url_kwarg = 'pub_pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeautyDetailView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context


class BeautyIndexView(generic.TemplateView):
    template_name = 'index.html'
    # context_object_name = 'publication_list'
    # model = PublicationFood

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeautyIndexView, self).get_context_data(**kwargs)
        context['publications'] = Publication.objects.all()
        return context


class BeautyAboutView(generic.TemplateView):
    template_name = 'about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeautyAboutView, self).get_context_data(**kwargs)
        context['about_list'] = Workers.objects.all()
        return context


class BeautyServiceView(generic.TemplateView):
    template_name = 'services.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeautyServiceView, self).get_context_data(**kwargs)
        context['service'] = Services.objects.all()
        return context


class BeautyWorkView(generic.TemplateView):
    template_name = 'work.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeautyWorkView, self).get_context_data(**kwargs)
        context['works'] = OurWork.objects.all()
        return context


class BeautyContactView(generic.TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BeautyContactView, self).get_context_data(**kwargs)
        context['publications'] = Publication.objects.all()
        return context


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
            return HttpResponse(content='данные успешно отпрвлены.')
        else:

            return HttpResponse(content=f'Похоже вы неправильно заполнили форму: {email_form.errors}')

#
# def add_comment_publication(request, pk):#запрос
#     if request.method == 'POST': #запрос
#         post_request_data = request.POST
#         comment_form = CommentForm(post_request_data)
#         print('здесь значение рекуест пост ', request.POST)  #запрос
#         if comment_form.is_valid():
#             comment=Comment.objects.create(
#                 name=comment_form.data['name'],
#                 email=comment_form.data['email'],
#                 message=comment_form.data['message'],
#                 category_id=pk)
#
#             return HttpResponse(content='каментарий успешно добавлен.')
#         else:
#             return HttpResponse(content=f'покоже вы не правильно заполнили форму:{comment_form.errors}')


def create_booking_tour(request):
    if request.method == 'POST':
        post_request = request.POST
        email_form = SignInForm(post_request)
        if email_form.is_valid():
            booking = SignIn.objects.create(
                first_name=email_form.data['first_name'],
                last_name=email_form.data['last_name'],
                date=email_form.data['date'],
                phone=email_form.data['phone'],
                message=email_form.data['message']
                )
            return HttpResponse(content='данные успешно отпрвлены.')
        else:
            return HttpResponse(content=f'Похоже вы неправильно заполнили форму: {email_form.errors}')













# def create_booking_tour(request):
#     if request.method == "POST":
#         sign = SignIn.objects.all()
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             print(data)
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             context = {"sign": sign, 'form': form}
#             return render(request,"index.html",context)




# def get_my_all_public(request):
#     publications=Publication.objects.all()
#     categories = Category.objects.all()
#     context = {"publications":publications,"categories":categories}
#     return render(request,'index.html',context=context)
#
#
# def get_my_all(request):
#     publications=Publication.objects.filter()
#     context = {"publications":publications}
#     return render(request,"blog.html",context=context)
#
#
# def get_detail(request, pk):
#     try:
#         publication = Publication.objects.get(id=pk)
#         context = {"publication": publication}
#     except Publication.DoesNotExist:
#         raise Http404
#     return render(request,"blog-single.html",context=context)



#
# def send_signin(request):
#     if request.method == 'POST':
#         post_request = request.POST
#         email_form = SignInForm(post_request)
#         if email_form.is_valid():
#             comment = SignIn.objects.create(
#                 first_name=email_form.data['first_name'],
#                 last_name=email_form.data['last_name'],
#                 date=email_form.data['date'],
#                 phone=email_form.data['phone'],
#                 message=email_form.data['message']
#                 )
#             return HttpResponse(content='данные успешно отпрвлены.')
#         else:
#             return HttpResponse(content=f'Похоже вы неправильно заполнили форму: {email_form.errors}')
#
#
#