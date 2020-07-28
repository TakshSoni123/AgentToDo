from rest_framework import serializers
from .models import Agent, todo

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

class todoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = '__all__'