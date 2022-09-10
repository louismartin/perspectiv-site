from django.shortcuts import render, redirect

from perspectiv.budget_insight_api import get_client_id, get_manage_connections_url


def app(request):
    return render(request, "app/app.html")


def manage(request):
    manage_url = get_manage_connections_url(
        get_client_id(),
        request.user.budgetinsightuser.auth_token,
        # Redirect to home page after user has connected their bank account
        redirect_uri=request.build_absolute_uri("/"),
    )
    return redirect(manage_url)
