from django.urls import path, include


from parts.app.views.home import HomeTemplateView

urlpatterns = [
     
     path('', HomeTemplateView.as_view(),
          name = 'home_template_view'
         ),
]
