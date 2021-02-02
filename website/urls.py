
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('BM125.urls')),
    path('eng/',include('cveng.urls'))

]
