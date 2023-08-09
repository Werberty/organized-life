from rest_framework import serializers

from organizer.models import Card, Tasks

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id',
            'title',
            'created',
            'modified',
        ]


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'time_init',
            'phase',
            'title',
            'created',
            'modified',
        ]