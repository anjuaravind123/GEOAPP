from django.shortcuts import render

from bookapp.forms import CustomerForm
from bookapp.forms import BookmarkForm
from bookapp.forms import CustomerBookmarkForm
from .models import CustomerBookmark
from rest_framework import generics
from .serializers import custbookSerializer


class JointAPICreateView(generics.CreateAPIView):
    queryset = CustomerBookmark.objects.all()
    serializer_class = custbookSerializer
    permission_classes = []
    authentication_classes = []


def welcome(request):
    return render(request, "welcome.html")


def load_form(request):
    form = CustomerForm
    return render(request, "bookmark.html", {'form': form})


def load_custbookmark(request):
    form = CustomerBookmarkForm
    return render(request, "customermark.html", {'form': form})


def load_bookmark(request):
    form = BookmarkForm
    return render(request, "custbookmark.html", {'form': form})
