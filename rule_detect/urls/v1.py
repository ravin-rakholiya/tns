from rule_detect import views
from django.urls import path, re_path

urlpatterns = [
    path('fetchdata', views.FetchDataAPIView.as_view()),


    
    # path('all', views.CompleteChatListView.as_view()),
    # path('recent/contacts', views.RecentlyContacted.as_view()),
   ]