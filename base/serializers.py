from rest_framework_json_api import serializers
from base.models import Task

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('user_id', 'title', 'description','complete','created')


