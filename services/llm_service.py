from services.registry_service import RegistryService
from services.provider_service import ProviderService


class LLMService:

    def __init__(self):

        self.registry = RegistryService()

        self.provider = ProviderService()

    def overview(self):

        return {

            "default": self.provider.default_provider(),

            "providers": self.registry.list_models()

        }
