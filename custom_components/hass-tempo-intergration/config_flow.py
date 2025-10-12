from homeassistant import config_entries
from .const import DOMAIN


class TempoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Temop config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 1