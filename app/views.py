from django.shortcuts import render, redirect

from perspectiv.budget_insight_api import get_client_id, get_manage_connections_url, get_investments_df


def app(request):
    df_investments = get_investments_df(request.user.budgetinsightuser.auth_token)
    df_investments_html = df_investments.to_html(table_id="investments-table")
    return render(request, "app/app.html", {"df_investments_html": df_investments_html})


def manage(request):
    manage_url = get_manage_connections_url(
        get_client_id(),
        request.user.budgetinsightuser.auth_token,
        # Redirect to home page after user has connected their bank account
        redirect_uri=request.build_absolute_uri("/"),
    )
    return redirect(manage_url)
