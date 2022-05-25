from rest_framework import serializers
from miApp.models import entryModel

class EntrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    dateTime = serializers.DateTimeField()
    concept = serializers.CharField()
    value = serializers.FloatField()
    
    def create(self, validated_data):
        instance = entryModel()
        return self.update(instance, validated_data)
    
    def update(self, instance, validated_data):
        instance.dateTime = validated_data.get("dateTime")
        instance.concept = validated_data.get("concept")    
        instance.value = validated_data.get("value")
        
        instance.save()    
        return instance
