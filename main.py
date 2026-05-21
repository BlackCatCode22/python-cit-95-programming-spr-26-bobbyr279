import time
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import requests

app = FastAPI(title="Global Weather Analytics")

# Strict User-Agent header for NWS requests
HEADERS = {"User-Agent": "FCC-Student-App"}


def get_us_weather(city_name, lat, lon):
    """Fetches data from the US National Weather Service API."""
    # Strict string concatenation to completely eliminate Markdown link parsing issues
    point_url = "https://api.weather.gov/points/" + str(lat) + "," + str(lon)
    try:
        point_response = requests.get(point_url, headers=HEADERS, timeout=5)
        point_response.raise_for_status()
        forecast_url = point_response.json()["properties"]["forecast"]

        time.sleep(0.1)  # Rate limit safety delay

        forecast_response = requests.get(forecast_url, headers=HEADERS, timeout=5)
        forecast_response.raise_for_status()
        current_period = forecast_response.json()["properties"]["periods"][0]

        return {
            "city": city_name,
            "temperature": current_period["temperature"],
            "unit": current_period["temperatureUnit"],
            "condition": current_period["shortForecast"],
            "details": current_period["detailedForecast"],
        }
    except Exception as e:
        return {
            "city": city_name,
            "temperature": "--",
            "unit": "F",
            "condition": "Error",
            "details": f"NWS Service Unavailable: {str(e)}",
        }


def get_global_weather(city_name, lat, lon):
    """Fetches global data from Open-Meteo API (No key required)."""
    # Open-Meteo returns metric by default; we append current=weather_code,temperature_2m
    # and temperature_unit=fahrenheit to keep dashboard values uniform
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,weather_code&temperature_unit=fahrenheit&wind_speed_unit=mph"

    # Weather Code translation mapping (WMO standards)
    wmo_codes = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing Rime Fog",
        51: "Light Drizzle",
        61: "Slight Rain",
        71: "Slight Snow",
        95: "Thunderstorm",
    }

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()["current"]

        code = data["weather_code"]
        condition_str = wmo_codes.get(
            code, "Unsettled" if code > 3 else "Clear Sky"
        )

        return {
            "city": city_name,
            "temperature": round(data["temperature_2m"]),
            "unit": "F",
            "condition": condition_str,
            "details": f"International data synchronized successfully via Open-Meteo node at coordinates [{lat}, {lon}].",
        }
    except Exception as e:
        return {
            "city": city_name,
            "temperature": "--",
            "unit": "F",
            "condition": "Error",
            "details": f"Global API connection failure: {str(e)}",
        }


@app.get("/", response_class=HTMLResponse)
async def dashboard_root():
    # Structural database coordinates
    us_cities = [
        {"name": "Fresno, CA", "lat": 36.7468, "lon": -119.7726},
        {"name": "New York, NY", "lat": 40.7128, "lon": -74.0060},
    ]
    global_cities = [{"name": "London, UK", "lat": 51.5074, "lon": -0.1278}]

    compiled_weather = []

    # Process domestic endpoints
    for city in us_cities:
        compiled_weather.append(
            get_us_weather(city["name"], city["lat"], city["lon"])
        )

    # Process international endpoints
    for city in global_cities:
        compiled_weather.append(
            get_global_weather(city["name"], city["lat"], city["lon"])
        )

    # Dynamic component compilation
    cards_html = ""
    for data in compiled_weather:
        cards_html += f"""
        <div class="metric-card">
            <div class="card-meta">
                <span class="location-title">{data['city']}</span>
                <span class="status-indicator"></span>
            </div>
            <div class="metric-display">
                <span class="value">{data['temperature']}</span>
                <span class="unit">°{data['unit']}</span>
            </div>
            <div class="weather-tag">{data['condition']}</div>
            <p class="summary-text">{data['details']}</p>
        </div>
        """

    # High-end, cohesive web layout template
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Enterprise Weather Network</title>
        <style>
            :root {{
                --background: #09090b;
                --surface: #121214;
                --border: #27272a;
                --text-primary: #f4f4f5;
                --text-secondary: #a1a1aa;
                --accent-cyan: #22d3ee;
            }}

            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}

            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
                background-color: var(--background);
                color: var(--text-primary);
                min-height: 100vh;
                padding: 4rem 2rem;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}

            header {{
                width: 100%;
                max-width: 1200px;
                margin-bottom: 4rem;
                border-left: 3px solid var(--accent-cyan);
                padding-left: 1.5rem;
            }}

            header h1 {{
                font-size: 2.25rem;
                font-weight: 700;
                letter-spacing: -0.04em;
                color: #ffffff;
            }}

            header p {{
                color: var(--text-secondary);
                font-size: 0.95rem;
                margin-top: 0.25rem;
            }}

            .grid-container {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
                gap: 2rem;
                width: 100%;
                max-width: 1200px;
            }}

            .metric-card {{
                background-color: var(--surface);
                border: 1px solid var(--border);
                border-radius: 16px;
                padding: 2.5rem;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
                transition: border-color 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            }}

            .metric-card:hover {{
                border-color: var(--accent-cyan);
            }}

            .card-meta {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 2rem;
            }}

            .location-title {{
                font-size: 1.25rem;
                font-weight: 600;
                letter-spacing: -0.02em;
            }}

            .status-indicator {{
                width: 8px;
                height: 8px;
                background-color: var(--accent-cyan);
                border-radius: 50%;
                box-shadow: 0 0 12px var(--accent-cyan);
            }}

            .metric-display {{
                display: flex;
                align-items: flex-start;
                margin-bottom: 1rem;
            }}

            .metric-display .value {{
                font-size: 5rem;
                font-weight: 700;
                line-height: 1;
                letter-spacing: -0.05em;
            }}

            .metric-display .unit {{
                font-size: 1.75rem;
                color: var(--text-secondary);
                margin-left: 0.25rem;
                font-weight: 400;
            }}

            .weather-tag {{
                align-self: flex-start;
                background-color: rgba(34, 211, 238, 0.08);
                color: var(--accent-cyan);
                border: 1px solid rgba(34, 211, 238, 0.15);
                padding: 0.35rem 0.85rem;
                border-radius: 100px;
                font-size: 0.8rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                margin-bottom: 2rem;
            }}

            .summary-text {{
                color: var(--text-secondary);
                font-size: 0.9rem;
                line-height: 1.6;
            }}

            @media (max-width: 480px) {{
                body {{
                    padding: 2rem 1rem;
                }}
                .metric-card {{
                    padding: 1.75rem;
                }}
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Global Node Weather Telemetry</h1>
            <p>Live data retrieval across synchronized national and international forecast networks.</p>
        </header>

        <main class="grid-container">
            {cards_html}
        </main>
    </body>
    </html>
    """
    return HTMLResponse(content=html_template, status_code=200)
