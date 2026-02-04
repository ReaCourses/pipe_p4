from prometheus_client.core import GaugeMetricFamily

class OrderByDeliveryTypeCollector:
    def collect(self):
        from django.db.models import Count
        from .models import Order

        metric = GaugeMetricFamily(
            'shop_orders_by_delivery_type',
            'Число заказов по типу доставки',
            labels=['delivery_type'],
        )

        for row in Order.objects.values('delivery_type').annotate(count=Count('id')):
            metric.add_metric([row['delivery_type']], float(row['count']))

        existing = {row['delivery_type'] for row in Order.objects.values('delivery_type')}

        for code, _ in Order.TYPE_DELIVERY:
            if code not in existing:
                metric.add_metric([code], 0.0)
        
        yield metric