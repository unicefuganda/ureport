#BROKER_URL = 'amqp://guest:guest@localhost:5672//'

CELERY_IMPORTS = ("message_classifier.tasks", )
CELERY_RESULT_BACKEND = 'amqp'
CELERY_RESULT_PERSISTENT = True
CELERY_TASK_RESULT_EXPIRES = None

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = {
    'default': {
        'binding_key': 'task.#',
    },
    'message_classifier.tasks.HandleExcelClassification': {
        'binding_key': 'upload.#',
    },
    'message_classifier.tasks.UploadResponsesTask': {
        'binding_key': 'poll.#',
    },
}
CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'

BROKER_HOST = "127.0.0.1"
BROKER_PORT = 5672
BROKER_USER = "ureport"
BROKER_PASSWORD = "ureport"
BROKER_VHOST = "ureport"

AMQP_SERVER = "127.0.0.1"
AMQP_PORT = 5672
AMQP_USER = "ureport"
AMQP_PASSWORD = "ureport"
AMQP_VHOST = "ureport"
