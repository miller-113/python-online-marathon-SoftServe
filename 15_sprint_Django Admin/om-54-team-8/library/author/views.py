# Create your views here.
from django.shortcuts import render
from . import models


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
