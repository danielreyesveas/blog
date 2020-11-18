from django.urls import path
from . import views
from .views import PostListView, MyPostListView, BookmarkPostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeactivateView, \
    UserView, UserPostListView, PostsByCategory, PostsByTag, PostsByDate, vote, bookmark, ajax_form

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('posts/', MyPostListView.as_view(), name='posts'),
    path('bookmarks/', BookmarkPostListView.as_view(), name='bookmarks'),
    path('category=<slug:category>', PostsByCategory.as_view(), name='post_by_category'),
    path('tag=<slug:tag>', PostsByTag.as_view(), name='post_by_tag'),
    path('date/<int:year>/<int:month>', PostsByDate.as_view(), name='post_by_date'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),

    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/new/', PostCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/deactivate/', PostDeactivateView.as_view(), name='post_deactivate'),
    
    path('ajax_form/', ajax_form, name="ajax_form"),
    path('vote/<int:pk>/<slug:slug>', vote, name="vote"),
    path('bookmark/<int:pk>', bookmark, name="bookmark"),


    

    path('profile/<str:slug>/', UserView.as_view(), name='user_profile'),
    path('message/', views.about, name='message'),
    
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]