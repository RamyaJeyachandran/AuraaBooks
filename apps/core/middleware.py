class TenantMiddleware:
    """
    Placeholder middleware — tenant functionality removed.
    Kept for compatibility; passes requests through unchanged.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
