from .models import Class

def common(request):
    context ={
        'class_list':Class.objects.all(),
    }
    return context