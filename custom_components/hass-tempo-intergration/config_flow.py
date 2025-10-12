from homeassistant import config_entries
from .const import DOMAIN


class TempoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Temop config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 1

    def __init__(self) -> None:
        """Init the ConfigFlow."""
        self.data: ConfigType = {}
    
    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> OptionsFlow:
        """Options callback for Eaton UPS."""
        return OptionsFlow(config_entry)


class OptionsFlow(config_entries.OptionsFlow):
    """Handle a options flow."""

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize options flow."""
        self.data = dict(entry.data)