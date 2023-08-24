from rest_framework import viewsets
from news_rest.serializers.user_serializer import UsersSerializer
from news.models.user_model import Users


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
