"""Platform for sensor integration."""
from __future__ import annotations
import requests
import datetime

from homeassistant.components.sensor import (
    SensorEntity,
)
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType



from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo

# The domain of your component
from .const import DOMAIN 

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up the sensor platform."""
    
    # Add your sensor entity
    async_add_entities([TodaySensor(entry), TomorrowSensor(entry)], True)




class TodaySensor(SensorEntity):
    """Todays Day Colour."""

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the sensor."""
        self._attr_name = "Todays Tempo Colour" # Name shown in the UI
        self._attr_unique_id = f"today_tempo_colour"
        self._state = self.get_state() # Initial state
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="Todays Tempo Colour",
            manufacturer="EDF",
            model="EDF Tempo",
        )

    @property
    def native_value(self):
        """Return the state of the sensor."""
        # This is where you'd fetch or calculate your sensor's value
        return self._state

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return "mdi:check-circle-outline"
        
    def get_state(self) -> str:
        """Fetch new state data for the sensor.
        """
        day_colour = "Unknown"
        if datetime.datetime.now().time() < datetime.time(6):
            today = datetime.date.today()
            previous_day = today - datetime.timedelta(days=1)
            formatted_url = previous_day.strftime('https://www.api-couleur-tempo.fr/api/jourTempo/%Y-%m-%d')
            response = requests.get(formatted_url)
            data = response.json()
            day_colour = data['libCouleur']
        else:
            response = requests.get("https://www.api-couleur-tempo.fr/api/jourTempo/today")
            data = response.json()
            day_colour = data['libCouleur']

        return day_colour

    async def async_update(self) -> None:
        """Fetch new state data for the sensor.
        
        This is the only method that should fetch new data for the entity.
        It runs on an interval set by HA's core update logic, or when explicitly requested.
        """
        self._state = self.get_state()


class TomorrowSensor(SensorEntity):
    """Tomorrow Day Colour."""

    def __init__(self, entry: ConfigEntry) -> None:
        """Initialize the sensor."""
        self._attr_name = "Tomorrow Colour" # Name shown in the UI
        self._attr_unique_id = f"tomorrow_tempo_colour"
        self._state = self.get_state() # Initial state
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="Tomorrow Tempo Colour",
            manufacturer="EDF",
            model="EDF Tempo",
        )

    @property
    def native_value(self):
        """Return the state of the sensor."""
        # This is where you'd fetch or calculate your sensor's value
        return self._state

    @property
    def icon(self):
        """Return the icon to use in the frontend."""
        return "mdi:check-circle-outline"
        
    def get_state(self) -> str:
        """Fetch new state data for the sensor.
        """
        response = requests.get("https://www.api-couleur-tempo.fr/api/jourTempo/tomorrow")
        data = response.json()
        day_colour = "Not Set Yet"
        if data['codeJour'] != 0:
            day_colour = data['libCouleur']
        
        return day_colour

    async def async_update(self) -> None:
        """Fetch new state data for the sensor.
        
        This is the only method that should fetch new data for the entity.
        It runs on an interval set by HA's core update logic, or when explicitly requested.
        """
        self._state = self.get_state()



# async def async_setup_entry(
#     hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
# ) -> None:
#     """Set up the sensors."""

#     coordinator = entry.runtime_data
#     entities: list[SensorEntity] = [
#         TodaySensor(coordinator),
#         TomorrowSensor(coordinator),
#     ]
#     async_add_entities(entities)


# def setup_platform(
#     hass: HomeAssistant,
#     config: ConfigType,
#     add_entities: AddEntitiesCallback,
#     discovery_info: DiscoveryInfoType | None = None
# ) -> None:
#     """Set up the sensor platform."""
#     add_entities([
#         TodaySensor(),
#         TomorrowSensor()
#         ])


# class TodaySensor(SensorEntity):
#     """Todays Day Colour."""

#     _attr_name = "Todays Colour"

#     def update(self) -> None:
#         """Fetch new state data for the sensor.
#         """
#         day_colour = "Unknown"
#         if datetime.datetime.now().time() < datetime.time(6):
#             today = datetime.date.today()
#             previous_day = today - datetime.timedelta(days=1)
#             formatted_url = previous_day.strftime('https://www.api-couleur-tempo.fr/api/jourTempo/%Y-%m-%d')
#             response = requests.get(formatted_url)
#             data = response.json()
#             day_colour = data['libCouleur']
#         else:
#             response = requests.get("https://www.api-couleur-tempo.fr/api/jourTempo/today")
#             data = response.json()
#             day_colour = data['libCouleur']

#         self._attr_native_value = day_colour

# class TomorrowSensor(SensorEntity):
#     """Tomorrow Day Colour."""

#     _attr_name = "Tomorrow Colour"

#     def update(self) -> None:
#         """Fetch new state data for the sensor.
#         """
#         response = requests.get("https://www.api-couleur-tempo.fr/api/jourTempo/tomorrow")
#         data = response.json()
#         day_colour = "Not Set Yet"
#         if data['codeJour'] != 0:
#             day_colour = data['libCouleur']
        
#         self._attr_native_value = day_colour