"""Platform for sensor integration."""
from __future__ import annotations
import requests
import datetime

from homeassistant.components.sensor import (
    # SensorDeviceClass,
    SensorEntity,
    # SensorStateClass,
)
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType


def setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None
) -> None:
    """Set up the sensor platform."""
    add_entities([
        TodaySensor(),
        TomorrowSensor()
        ])


class TodaySensor(SensorEntity):
    """Todays Day Colour."""

    _attr_name = "Todays Colour"

    def update(self) -> None:
        """Fetch new state data for the sensor.
        """
        day_colour = "Unknown"
        if (datetime.datetime.now().time() < datetime.time(6)) {
            import datetime
            today = datetime.date.today()
            previous_day = today - datetime.timedelta(days=1)
            formatted_url = previous_day.strftime('https://www.api-couleur-tempo.fr/api/jourTempo/%Y-%m-%d')
            response = requests.get(formatted_url)
            data = response.json()
            day_colour = data['libCouleur']
        } else {
            response = requests.get("https://www.api-couleur-tempo.fr/api/jourTempo/today")
            data = response.json()
            day_colour = data['libCouleur']
        }

        self._attr_native_value = day_colour

class TomorrowSensor(SensorEntity):
    """Tomorrow Day Colour."""

    _attr_name = "Tomorrow Colour"

    def update(self) -> None:
        """Fetch new state data for the sensor.
        """
        response = requests.get("https://www.api-couleur-tempo.fr/api/jourTempo/tomorrow")
        data = response.json()

        self._attr_native_value = data['libCouleur']