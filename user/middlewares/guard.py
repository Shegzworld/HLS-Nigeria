from django.http import JsonResponse
from functools import wraps

def role_required(required_role):
    """
    Middleware to check if the user's role matches the required role.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'Unauthorized'}, status=401)

            # Check the user's role
            user_role = getattr(request.user.profile, 'role', None)
            if user_role != required_role:
                return JsonResponse({'error': 'Forbidden: Insufficient Role'}, status=403)

            # Proceed to the view
            return view_func(request, *args, **kwargs)

        return _wrapped_view
    return decorator
