from celery.utils.log import get_task_logger
from core.celery import app

from apps.review.email import send_review_email

logger = get_task_logger(__name__)


@app.task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    """
    Task for sending an email to a user after they submit a review.
    """
    logger.info(f"Sending review email to {email}")
    return send_review_email(name, email, review)
