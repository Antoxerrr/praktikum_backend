from django_filters import CharFilter
from django_filters.rest_framework import FilterSet

from comments.models import CommentTemplate


class CommentsFilter(FilterSet):

    COMMON_KEYWORD = 'common'

    project_id = CharFilter(method='filter_project_id')

    def filter_project_id(self, queryset, name, value):
        if value == self.COMMON_KEYWORD:
            return queryset.filter(**{f'{name}__isnull': True})
        return queryset.filter(**{name: value})

    class Meta:
        model = CommentTemplate
        fields = ['project_id']
