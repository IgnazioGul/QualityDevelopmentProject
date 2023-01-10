import pytest
from src.services.index import get_message


def test_get_message():
    # Test with all possible fields present
    meteo = {
        'name': 'Paris',
        'main': {
            'temp': 28.4,
            'feels_like': 29.4,
            'temp_min': 26.0,
            'temp_max': 30.0,
            'pressure': 1013,
            'humidity': 45,
            'sea_level': 1023
        }
    }
    expected_message = "Che tempo fa a Paris?\n" \
                       "temp.: 28.4 C° 🌡\n" \
                       "temp. avvertita: 29.4 C° 🌡\n" \
                       "temp. min: 26.0 C° 🧊\n" \
                       "temp. max: 30.0 C° 🔥\n" \
                       "pressione: 1013\n" \
                       "umidità: 45% 💧\n" \
                       "livello del mare: 1023 🌊\n"
    assert get_message(meteo) == expected_message

    # Test with only required fields present
    meteo = {
        'main': {
            'temp': 28.4,
            'humidity': 45
        }
    }
    expected_message = "temp.: 28.4 C° 🌡\n" \
                       "umidità: 45% 💧\n"

    assert get_message(meteo) == expected_message

    # Test with empty meteo dictionary
    meteo = {}
    expected_message = ""
    assert get_message(meteo) == expected_message
    