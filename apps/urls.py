from django.urls import path
from django.contrib import admin
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    
path('admin/',admin.site.urls),
# path('drinks/',views.drink_list),
# path('drinks/<int:id>', views.drink_detail),

]
urlpatterns = format_suffix_patterns(urlpatterns)
#now can use different extensions like .json with above urls