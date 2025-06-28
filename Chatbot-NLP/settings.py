INSTALLED_APPS = [
    ...
    'chat',
    'channels',
    'rest_framework',
]

ASGI_APPLICATION = 'chatbot_nlp.asgi.application'

# Redis for Channels
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}

