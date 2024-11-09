from django.urls import path
from newspaper import views
from .views import ContactView, PostDetailView, CommentView, PostSearchView, NewsletterView

urlpatterns = [
    path('', views.HomeView.as_view(), name ="home" ),
    path("about/", views.AboutView.as_view(), name="about" ),
    path('contact/', ContactView.as_view(), name='contact'),
    path("post-list/", views.PostListView.as_view(), name="post-list" ),
    path("post-by-category/<int:category_id>/", views.PostByCategoryView.as_view(), name="post-by-category"),
    path("post-by-tag/<int:tag_id>/", views.PostByTagView.as_view(), name="post-by-tag"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post-comment/", views.CommentView.as_view(), name="post-comment"),
    path("post-search/", views.PostSearchView.as_view(), name="post-search"),
    path("newsletter/", views.NewsletterView.as_view(), name="newsletter"),
]