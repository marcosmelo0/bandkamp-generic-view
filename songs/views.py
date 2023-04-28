from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView


class PaginationSong(PageNumberPagination):
    page_size = 1


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = (PaginationSong)

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs.get("pk"))

        serializer.save(album=album)
