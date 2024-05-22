from rest_framework import serializers
from .models import SearchTerm

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchTerm
        fields = ['key']
