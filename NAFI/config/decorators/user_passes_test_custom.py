from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from functools import wraps

def user_passes_test_custom(test_func, login_url=None, redirect_field_name='next'):
    """
    Decorator that checks if the user passes a custom test function. If the user does not pass the test,
    it redirects them to the 'error_page'. If the user passes the test, it calls the original view function
    with the provided arguments and keyword arguments.

    Args:
        test_func (function): The custom test function that takes a user object as an argument and returns a boolean.
        login_url (str, optional): The URL to redirect the user to if they are not authenticated. Defaults to None.
        redirect_field_name (str, optional): The name of the field to store the redirect URL in case of redirection.
            Defaults to 'next'.

    Returns:
        function: The decorated view function.

    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                return redirect('error_page')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
