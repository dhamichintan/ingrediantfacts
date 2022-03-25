from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',include('product.urls')),
    path('group/', include('group.urls')),
]
