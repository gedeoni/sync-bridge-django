from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from common.responses import ok
from common.monitoring import monitored
from .serializers import SyncRequestSerializer
from .services import sync_payload
from sync_history.models import SyncHistory


class SyncView(APIView):
    @monitored('sync.operation', tags=['model'])
    def post(self, request):
        serializer = SyncRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        payload = serializer.validated_data
        result = sync_payload(payload['model'], payload['data'])
        return Response(ok('Sync successful', result))


class SyncStatsView(APIView):
    @monitored('sync.stats')
    def get(self, request):
        rows = SyncHistory.objects.values('status').annotate(count=Count('id'))
        summary = {}
        total = 0
        for row in rows:
            summary[row['status']] = row['count']
            total += row['count']
        summary['total'] = total
        return Response(ok('Sync stats retrieved successfully', summary))
