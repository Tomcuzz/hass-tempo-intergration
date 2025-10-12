import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_NAME

# The domain of your component
DOMAIN = "my_sensor_integration"

class MySensorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for My Sensor Integration."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        # This step is called when the user starts the integration setup.
        
        # Check if an instance already exists (optional, but good practice for no-input setups)
        # If you only want ONE instance of this sensor, uncomment the next block:

        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        
        if user_input is not None:
            # If the flow has reached this point, it means the user clicked 'SUBMIT'
            # on a default (empty) form or we are simulating the completion.
            
            # Since we need NO inputs, we immediately create the config entry.
            return self.async_create_entry(
                title="Tempo Sensor",
                data={} # Empty data dictionary as no input was gathered
            )

        # Show the default form. Since we haven't provided a schema, it'll be a 
        # single 'SUBMIT' button, effectively.
        return self.async_show_form(step_id="user")

# from __future__ import annotations

# from homeassistant import config_entries
# from homeassistant.core import callback
# from homeassistant.config_entries import ConfigEntry
# from .const import DOMAIN


# class TempoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
#     """Temop config flow."""
#     # The schema version of the entries that it creates
#     # Home Assistant will call your migrate method if the version changes
#     VERSION = 1
#     MINOR_VERSION = 1

#     def __init__(self) -> None:
#         """Init the ConfigFlow."""
#         self.data: ConfigType = {}
    
#     @staticmethod
#     @callback
#     def async_get_options_flow(
#         config_entry: ConfigEntry,
#     ) -> OptionsFlow:
#         """Options callback for Eaton UPS."""
#         return OptionsFlow(config_entry)


# class OptionsFlow(config_entries.OptionsFlow):
#     """Handle a options flow."""

#     def __init__(self, entry: ConfigEntry) -> None:
#         """Initialize options flow."""
#         self.data = dict(entry.data)