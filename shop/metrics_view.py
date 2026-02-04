from django.http import HttpResponse

def prometheus_metrics_view(_request):
    from prometheus_client import CollectorRegistry, CONTENT_TYPE_LATEST, generate_latest
    from prometheus_client import multiprocess
    from os import getenv

    registry = CollectorRegistry()

    if getenv('PROMETHEUS_MULTIPROC_DIR'):
        multiprocess.MultiProcessCollector(registry)

    from .metrics import OrderByDeliveryTypeCollector
    registry.register(OrderByDeliveryTypeCollector())

    output = generate_latest(registry)
    return HttpResponse(output, content_type=CONTENT_TYPE_LATEST)
