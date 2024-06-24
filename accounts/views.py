from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def create_account(request):
    # Create a new user account
    if request.method != 'POST':
        # Display black create account form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to home page
            login(request, new_user)
            return redirect('worksrepo:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/create_account.html', context)


