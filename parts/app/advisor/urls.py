from django.urls import path

from parts.app.views import advisor


app_name = 'advisor'

urlpatterns = [
    path('/create/advisor/',
        advisor.AdvisorCreateView.as_view(),
        name='advisor_create'    
    )
]