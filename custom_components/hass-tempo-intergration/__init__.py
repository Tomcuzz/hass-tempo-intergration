from .const import DOMAIN, PLATFORMS

async def async_setup(hass, config):

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Return boolean to indicate that initialization was successful.
    return True