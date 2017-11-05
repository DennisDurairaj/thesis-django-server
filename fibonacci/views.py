from django.http import JsonResponse
from decimal import Decimal


def index(request):
    a, b = 1, 1
    result = 'result'
    for i in range(1400):
        a, b = b, a + b
    data = {result: '%.2E' % Decimal(a)}
    return JsonResponse(data)
