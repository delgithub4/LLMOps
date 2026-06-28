from providers.openai_provider import OpenAIProvider
from providers.anthropic_provider import AnthropicProvider
from providers.local_provider import LocalProvider


class RegistryService:

    def __init__(self):

        self.providers = [

            OpenAIProvider(),

            AnthropicProvider(),

            LocalProvider()

        ]

    def list_models(self):

        return [

            provider.info()

            for provider in self.providers

        ]
