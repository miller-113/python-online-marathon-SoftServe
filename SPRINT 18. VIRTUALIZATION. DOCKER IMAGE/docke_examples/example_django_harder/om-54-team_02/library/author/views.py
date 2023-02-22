from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView
from rest_framework import viewsets
from rest_framework.response import Response

from .forms import *
from . import models
from .serializers import AuthorsSerializer


def create_author(request):
    if request.method == 'POST':
        data = request.POST
        author = models.Author.create(data['name'],
                                      data['surname'],
                                      data['patronymic'])
        return render(request, 'author/create_author.html', {'author': author})
    return render(request, 'author/create_author.html')


# show information about all authors (librarian)
def show_authors(request):
    authors = models.Author.get_all()
    return render(request, 'author/show_authors.html', {'authors': authors})


# provide the ability to remove the author if he is not attached to
# any book (librarian)
def remove_author(request):
    authors = models.Author.get_all()
    if request.method == 'POST':
        author_id = request.POST['authors']
        if author_id != 'False':
            author = models.Author.objects.get(id=author_id)
            if not len(author.books.all()):
                models.Author.delete_by_id(author_id)
                authors = models.Author.get_all()
            return render(request, 'author/remove_author.html',
                      {'authors': authors,
                       'deleted_author': author})

    return render(request, 'author/remove_author.html', {'authors': authors})


class AuthorFormView(FormView):
    """Serves for transition of information from front-end into form of model Author"""
    form_class = AuthorFormModel
    template_name = 'author/create_author.html'
    success_url = '/author/create_author/success/'


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def success_author_creation(request):
    """Notification in case of successful creation of a new author."""
    return HttpResponse("<script>alert ('Congratulations! The author was successfully created!'); "
                        "window.location = '/author/show_authors/';</script>")


def update_author(request, author_id=None):
    if author_id:
        try:
            author = Author.objects.get(pk=author_id)
        except:
            return redirect('/author/show_authors/')
        else:
            form = UpdateAuthorFormModel(initial=
                                        {'name': author.name,
                                         'surname': author.surname,
                                         'patronymic': author.patronymic,
                                         'books': author.books,
                                         })

            if request.method == 'POST':
                form = UpdateAuthorFormModel(request.POST)

                if form.is_valid():
                    data = form.cleaned_data
                    author.name = data.get('name')
                    author.surname = data.get('surname')
                    author.patronymic = data.get('patronymic')
                    author.save()
                    print("cleaned data:", form.cleaned_data)
                    return redirect('/author/show_authors/')

            else:
                return render(request, 'author/update_author.html', {'form': form})
    else:
        return redirect('/author/show_authors/')


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorsSerializer

    def list(self, request):
        context={'request': request}

        queryset = Author.objects.all()
        serializer = AuthorsSerializer(queryset, many=True, context=context)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, *args, **kwargs):
        context={'request': request}

        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorsSerializer(author, context=context)
        return Response(serializer.data)

#

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
#
#
# @csrf_exempt
# def authors_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Author.objects.all()
#         serializer = AuthorsSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = AuthorsSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def author_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Author.objects.get(pk=pk)
#     except Author.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = AuthorsSerializer(snippet)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = AuthorsSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)
