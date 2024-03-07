from mage_ai.authentication.oauth.constants import (
    AZURE_DEVOPS_ORGANIZATION,
    ProviderName,
)
from mage_ai.authentication.providers.active_directory import ADProvider


class AzureDevopsProvider(ADProvider):
    provider = ProviderName.AZURE_DEVOPS
    scope = '499b84ac-1321-427f-aa17-267ca6975798/.default'  # noqa: E501

    def __init__(self):
        super().__init__()
        if not AZURE_DEVOPS_ORGANIZATION:
            raise Exception(
                'Azure DevOps organization is empty. '
                'Make sure the AZURE_DEVOPS_ORGANIZATION environment variable is set.')
