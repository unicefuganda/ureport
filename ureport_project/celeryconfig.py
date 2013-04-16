#BROKER_URL = 'amqp://guest:guest@localhost:5672//'

#CELERY_ALWAYS_EAGER = True



CELERY_RESULT_BACKEND = 'amqp'
CELERY_RESULT_PERSISTENT = False
CELERY_TASK_RESULT_EXPIRES = 10
CELERY_DISABLE_RATE_LIMITS = True

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
    'start_poll': {
        'binding_key': 'start_poll.#',
        },
    'process_message': {
        'binding_key': 'process_message.#',
        },
    'handle_incoming': {
        'binding_key': 'handle_incoming.#',
        },
    'reprocess_responses': {
        'binding_key': 'reprocess_responses.#',
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
    'ureport.tasks.start_poll': {
        'queue': 'start_poll',
        'routing_key': 'start_poll.result'
    },
    'ureport.tasks.process_message': {
        'queue': 'process_message',
        'routing_key': 'process_message.result'
    },
    'rapidsms_httprouter.tasks.handle_incoming': {
        'queue': 'handle_incoming',
        'routing_key': 'handle_incoming.result'
    },
    'ureport.tasks.reprocess_responses': {
        'queue': 'reprocess_responses',
        'routing_key': 'reprocess_responses.result'
    },

}


CELERY_IMPORTS = ('tasks',)