from django.shortcuts import render
from .models import AAExam
from django.contrib.auth.models import User

def ipexam_list(request):
    current_user = request.user

    fio = f"{current_user.last_name} {current_user.first_name}" if current_user.is_authenticated else "Гость"
    group = current_user.groups.first().name if current_user.is_authenticated and current_user.groups.exists() else "Группа не указана"
    

    exams = AAExam.objects.filter(is_public=True).prefetch_related('users')
    
    context = {
        'exams': exams,
        'fio': fio,
        'group': group,
    }
    
    return render(request, 'task/ipexam_list.html', context)