from rest_framework import serializers
from todo.models import TodoItem

# serializers.HyperlinkedModelSerializer -> will automatically create hyperlinks
#   for the 'url' field in the TODO item.
class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.ReadOnlyField()
  class Meta:
    model = TodoItem

    # These are the fields that our model will expose
    fields = ('url', 'title', 'completed', 'order')
