urlpatterns = [
    path('', include('leads.urls')),
    path('', include('frontend.urls')),
]
