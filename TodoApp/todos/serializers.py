from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            "id", "title", "description", "is_completed",
            "due_date", "created_at", "updated_at"
        ]
        ready_only_fields = ["id", "created_at", "updated_at"]

