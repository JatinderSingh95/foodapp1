from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('server_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def server_list(request):
    
	
      return render(request, 'server_list.html')
	  
def pfbusi(request):
    
	
      return render(request, 'Addrest.html')	  
	  
def rest(request):
    
	
      return render(request, 'rest.html')	  	  