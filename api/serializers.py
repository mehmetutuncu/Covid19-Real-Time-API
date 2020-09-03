from rest_framework import serializers
from api.models import Covid19DailyData
from rest_framework.exceptions import ValidationError

class DailyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Covid19DailyData
        fields = '__all__'


class QueryStringSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, default=1)
    item_per_page = serializers.IntegerField(required=False, default=10)
    start_date = serializers.DateField(required=False, format='%Y-%m-%d')
    end_date = serializers.DateField(required=False, format='%Y-%m-%d')
    filter = serializers.ChoiceField(required=False, choices=['range', 'lte', 'gte', 'equals'])

    def validate_filter(self, filter):
        start_date = self.initial_data.get('start_date')
        end_date = self.initial_data.get('end_date')
        if filter == 'range':
            if start_date is None or end_date is None:
                raise ValidationError("start_date and end_date required for range query.")
        else:
            if start_date is None:
                raise ValidationError(f"start_date required for {filter} query.")
        return filter
