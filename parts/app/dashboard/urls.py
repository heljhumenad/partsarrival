from django.urls import path

from parts.app.views import dashboard

app_name = 'dashboard'

urlpatterns = [

    path('dashboard/index',
         dashboard.DashboardViewsTemplate.as_view(),
         name="dashboard_view_index"
         ),

]
