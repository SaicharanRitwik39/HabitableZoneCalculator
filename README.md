# HabitableZoneCalculator

This web application calculates the habitable zone (HZ) for a given star system using user input for the star's luminosity, semi-major axis of the planet's orbit, and the star's temperature. The app determines whether a planet is within the habitable zone based on the definitions provided by Kopparapu et al. (2014).

Features
* User Input:

    *Star's Luminosity (Lsun): Input the luminosity of the star in solar units.
Semi-Major Axis (AU): Input the semi-major axis of the planet's orbit in astronomical units.
Star's Temperature (K): Input the temperature of the star in Kelvin.
Calculations:

Calculates the stellar flux for the given inputs.
Determines the habitable zone boundaries based on the star's temperature for the following zones:
Recent Venus
Runaway Greenhouse
Maximum Greenhouse
Early Mars
Results Display:

Effective stellar flux (Seff) for the given inputs.
Distances in astronomical units (AU) for the boundaries of the habitable zones.
Indicates whether the planet is in the habitable zone:
Optimistic Habitable Zone (between Maximum Greenhouse and Early Mars or between Recent Venus and Runaway Greenhouse)
Conservative Habitable Zone (between Runaway Greenhouse and Maximum Greenhouse)
Beyond Early Mars (not in the habitable zone)

The app is live at https://hzcalc.streamlit.app/
