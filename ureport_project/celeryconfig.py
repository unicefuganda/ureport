#BROKER_URL = 'amqp://guest:guest@localhost:5672//'

#CELERY_ALWAYS_EAGER = True



CELERY_RESULT_BACKEND = 'amqp'
CELERY_RESULT_PERSISTENT = True
CELERY_TASK_RESULT_EXPIRES = None

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = {
    'default': {
        'binding_key': 'task.#',
    },
    'upload_responses': {
        'binding_key': 'upload_responses.#',
    },
    'classify_excel': {
        'binding_key': 'classify_excel.#',
    },
    'message_export': {
           'binding_key': 'message_export.#',
       },
}
CELERY_DEFAULT_EXCHANGE = 'tasks'
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = 'task.default'
#CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"

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




CELERY_ROUTES = {
    'message_classifier.tasks.upload_responses': {
        'queue': 'upload_responses',
        'routing_key': 'upload_responses.result'
    },
    'message_classifier.tasks.classify_excel': {
           'queue': 'classify_excel',
           'routing_key': 'classify_excel.result'
       },
    'message_classifier.tasks.message_export': {
           'queue': 'message_export',
           'routing_key': 'message_export.result'
       },

}
