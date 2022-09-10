from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from perspectiv.budget_insight_api import get_client_id, get_client_secret, create_new_user

from .forms import UserRegisterForm, UserUpdateForm
from .models import BudgetInsightUser


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print("form is valid")
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            user = form.save()
            # TODO: Should this logic happen on user creation with a custom class?
            budget_insight_user_id, budget_insight_auth_token = create_new_user(get_client_id(), get_client_secret())
            budget_insight_user = BudgetInsightUser.objects.create(
                app_user=user, user_id=budget_insight_user_id, auth_token=budget_insight_auth_token
            )
            budget_insight_user.save()
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'users/profile.html', context)