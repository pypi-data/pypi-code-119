from ssb_altinn3_util.clients.auth.altinn_auth_client_config import AltinnAuthClientConfig
from ssb_altinn3_util.clients.auth.helpers.altinn_client import AltinnClient
from ssb_altinn3_util.clients.auth.helpers.guardian_client import GuardianClient
from ssb_altinn3_util.clients.auth.helpers.keycloak_client import KeycloakClient
from ssb_altinn3_util.clients.auth.helpers.secret_manager_client import SecretManagerClient


class AltinnAuthClient:
    def __init__(self, config: AltinnAuthClientConfig):
        self.secret_client = SecretManagerClient(config.keycloak_secret_path)
        self.keycloak_client = KeycloakClient(config.platform_environment)
        self.guardian_client = GuardianClient(config.platform_environment)
        self.altinn_client = AltinnClient(config.altinn_base_url)
        self.maskinport_client_id = config.maskinport_client_id

    def get_altinn_auth_token(self) -> str:
        keycloak_secret = self.secret_client.get_secret()
        keycloak_token = self.keycloak_client.get_token(self.maskinport_client_id, keycloak_secret)
        maskinport_token = self.guardian_client.get_token(keycloak_token)
        altinn_token = self.altinn_client.get_altinn_token(maskinport_token)

        return altinn_token
