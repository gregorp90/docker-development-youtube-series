import logging
import time

from fluent import handler as fluent_handler, sender

logger = logging.getLogger()
logger.setLevel(logging.INFO)

h = fluent_handler.FluentHandler(
    "app",
    host="localhost",
    port=int(24224),
    nanosecond_precision=True,
)

logger.addHandler(h)

log_handler = logging.StreamHandler()
logger.addHandler(log_handler)

while True:
    logger.info("Send log")
    time.sleep(5)

