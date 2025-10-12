from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, PLATFORMS

async def async_setup(hass: HomeAssistant, entry: ConfigEntry):

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Return boolean to indicate that initialization was successful.
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)