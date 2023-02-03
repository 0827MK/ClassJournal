from django.views import generic
from django.shortcuts import render
from .models import Record

class IndexView(generic.ListView):
    model = Record
    def get_queryset(self):
        #並び替え：作成日が新しい順に並べる
        return Record.objects.order_by('-created_at')

class DetailView(generic.DetailView):
    model=Record
    
def index(request):
    return render(request, 'employee/base.html')