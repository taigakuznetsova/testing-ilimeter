from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Notification

@login_required
def user_notifications(request):
    """
    Renders the user's notifications page.

    This view is decorated with `@login_required` to ensure that the user is authenticated before accessing the page. It retrieves all the notifications for the current user, ordered by their creation date in descending order. The retrieved notifications are then passed to the `user_notifications.html` template for rendering.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response containing the user's notifications.
    """
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications/user_notifications.html', {'notifications': notifications})

@login_required
def mark_notification_as_read(request, notification_id):
    """
    Mark a notification as read.

    This function is decorated with `@login_required` to ensure that the user is authenticated before
    accessing this view. It takes in a `request` object and a `notification_id` as parameters.

    Parameters:
        request (HttpRequest): The HTTP request object.
        notification_id (int): The ID of the notification to be marked as read.

    Returns:
        HttpResponseRedirect: A redirect to the `user_notifications` URL.

    Raises:
        Notification.DoesNotExist: If the notification with the specified ID does not exist.

    """
    notification = Notification.objects.get(id=notification_id, user=request.user)
    if notification:
        notification.read = True
        notification.save()
    return redirect('user_notifications')