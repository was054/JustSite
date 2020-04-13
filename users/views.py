from django.shortcuts import render
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'user/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        #user_form.fields['username'].help_text='Govno'      Тут можно отредачить подсказку для username
    return render(request, 'user/registration.html', {'user_form': user_form})
