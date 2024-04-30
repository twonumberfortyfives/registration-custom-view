def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ['username', 'email', 'first_name', 'last_name']
