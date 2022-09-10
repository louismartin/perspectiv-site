from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from perspectiv.budget_insight_api import get_client_id, get_manage_connections_url, get_investments_df


@login_required
def app(request):
    df_investments = get_investments_df(request.user.budgetinsightuser.auth_token)
    # TODO: Display nothing when there are no accounts connected
    context = {}
    if df_investments is not None:
        context["df_investments_html"] = df_investments.to_html(table_id="investments-table")
        context["total_valuation"] = df_investments["valuation"].sum()
    return render(request, "app/app.html", context)


@login_required
def manage(request):
    manage_url = get_manage_connections_url(
        get_client_id(),
        request.user.budgetinsightuser.auth_token,
        # Redirect to home page after user has connected their bank account
        redirect_uri=request.build_absolute_uri("/"),
    )
    return redirect(manage_url)
