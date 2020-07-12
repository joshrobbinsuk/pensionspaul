from rest_framework import serializers
from funds.models import Fund



class CompareFundSerializer(serializers.Serializer):
    potsize = serializers.IntegerField(max_value=1000000,min_value=1)
    years = serializers.IntegerField(max_value=99,min_value=1)
    drawdown = serializers.IntegerField(max_value=99,min_value=0)


# NOT USED AT PRESENT
class FundSerializer(serializers.ModelSerializer):
    # final_pot = serializers.SerializerMethodField()

    class Meta:
        model = Fund
        fields = ["brand", "fund_type"]

    # def get_final_pot(self, obj):
    # return self.context


