from rest_framework import viewsets, mixins


class CreateListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """Позволяет создавать объект и просматривать список всех объектов."""

    pass
