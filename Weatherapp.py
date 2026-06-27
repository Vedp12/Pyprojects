"""
Weather Report App
==================
Fetches current weather for a city using OpenWeatherMap API,
saves results to CSV history, and generates a PDF report.

Requirements:
    pip install requests reportlab

API Key:
    Sign up at https://openweathermap.org/api to get your free API key.
    Replace API_KEY below with your actual key.
"""

import csv
import os
import requests
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

# ──────────────────────────────────────────
#  CONFIGURATION  –  put your key here
# ──────────────────────────────────────────
API_KEY = "5a151cc7b64cc481acc06c5c1f0a0c13"   # ← replace this
BASE_URL =f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={API_KEY}"
NEWS_URL = "https://api.openweathermap.org/data/2.5/find"       # city search (reuse key)

CSV_FILE  = "weather_history.csv"
PDF_DIR   = "reports"
CSV_HEADERS = [
    "timestamp", "city", "country",
    "temperature_c", "feels_like_c",
    "humidity_pct", "description",
    "wind_speed_ms", "visibility_m",
]

# ──────────────────────────────────────────
#  WEATHER FETCHING
# ──────────────────────────────────────────

def fetch_weather(city: str) -> dict:
    """Call OpenWeatherMap current-weather endpoint and return parsed data."""
    params = {
        "q":     city,
        "appid": API_KEY,
        "units": "metric",   # Celsius
    }
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if resp.status_code == 401:
            raise SystemExit(
                "\n[ERROR] Invalid API key.\n"
                "Get a free key at https://openweathermap.org/api\n"
                f"Then set API_KEY in {__file__}"
            )
        if resp.status_code == 404:
            raise SystemExit(f"\n[ERROR] City '{city}' not found. Check the spelling.")
        raise SystemExit(f"\n[ERROR] HTTP {resp.status_code}: {e}")
    except requests.exceptions.ConnectionError:
        raise SystemExit("\n[ERROR] No internet connection.")
    except requests.exceptions.Timeout:
        raise SystemExit("\n[ERROR] Request timed out.")

    raw = resp.json()
    return {
        "city":           raw["name"],
        "country":        raw["sys"]["country"],
        "temperature_c":  round(raw["main"]["temp"], 1),
        "feels_like_c":   round(raw["main"]["feels_like"], 1),
        "humidity_pct":   raw["main"]["humidity"],
        "description":    raw["weather"][0]["description"].title(),
        "wind_speed_ms":  raw["wind"]["speed"],
        "visibility_m":   raw.get("visibility", "N/A"),
        "timestamp":      datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

# ──────────────────────────────────────────
#  FAKE NEWS HEADLINES  (OpenWeatherMap
#  doesn't provide news; we generate
#  context-aware weather headlines instead)
# ──────────────────────────────────────────

def generate_headlines(data: dict) -> list[str]:
    """Create weather-themed news headlines from the fetched data."""
    city  = data["city"]
    temp  = data["temperature_c"]
    desc  = data["description"]
    hum   = data["humidity_pct"]
    wind  = data["wind_speed_ms"]

    headlines = [
        f"{city} Wakes Up to {desc} Skies This Morning",
        f"Temperatures in {city} Sitting at {temp}°C — {'Wrap Up!' if temp < 15 else 'Stay Cool!'}",
        f"Humidity Levels Reach {hum}% in {city} — {'Muggy Day Ahead' if hum > 70 else 'Comfortable Conditions'}",
        f"Wind Speeds of {wind} m/s Reported Across {city} Region",
        f"Weather Alert: {desc} Conditions Expected to {'Persist' if temp > 20 else 'Ease'} Through the Day",
    ]
    return headlines

# ──────────────────────────────────────────
#  CSV HISTORY
# ──────────────────────────────────────────

def save_to_csv(data: dict) -> None:
    """Append a search record to weather_history.csv."""
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
        if not file_exists:
            writer.writeheader()
        writer.writerow({k: data.get(k, "") for k in CSV_HEADERS})
    print(f"  ✔ History saved → {CSV_FILE}")


def load_history() -> list[dict]:
    """Return all rows from the CSV history file."""
    if not os.path.isfile(CSV_FILE):
        return []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# ──────────────────────────────────────────
#  PDF REPORT
# ──────────────────────────────────────────

def _style(name, **kwargs):
    base = getSampleStyleSheet()[name]
    return ParagraphStyle(name + "_custom", parent=base, **kwargs)


def generate_pdf(data: dict, headlines: list[str]) -> str:
    """Build a nicely formatted PDF report and return its file path."""
    os.makedirs(PDF_DIR, exist_ok=True)
    safe_city = data["city"].replace(" ", "_")
    ts_file   = datetime.now().strftime("%Y%m%d_%H%M%S")
    path      = os.path.join(PDF_DIR, f"weather_{safe_city}_{ts_file}.pdf")

    doc   = SimpleDocTemplate(path, pagesize=letter,
                              leftMargin=0.75*inch, rightMargin=0.75*inch,
                              topMargin=0.75*inch, bottomMargin=0.75*inch)
    story = []
    W     = letter[0] - 1.5*inch   # usable width

    # ── Header ────────────────────────────
    story.append(Paragraph(
        "🌤  Weather Report",
        _style("Title", fontSize=26, textColor=colors.HexColor("#1a73e8"), spaceAfter=4)
    ))
    story.append(Paragraph(
        f"Generated on {data['timestamp']}",
        _style("Normal", fontSize=10, textColor=colors.grey, spaceAfter=2)
    ))
    story.append(HRFlowable(width=W, thickness=1.5,
                             color=colors.HexColor("#1a73e8"), spaceAfter=16))

    # ── City banner ───────────────────────
    story.append(Paragraph(
        f"{data['city']}, {data['country']}",
        _style("Heading1", fontSize=20, textColor=colors.HexColor("#202124"), spaceAfter=2)
    ))
    story.append(Paragraph(
        data["description"],
        _style("Normal", fontSize=13, textColor=colors.HexColor("#5f6368"), spaceAfter=14)
    ))

    # ── Weather data table ─────────────────
    table_data = [
        ["Metric", "Value"],
        ["Temperature",  f"{data['temperature_c']} °C"],
        ["Feels Like",   f"{data['feels_like_c']} °C"],
        ["Humidity",     f"{data['humidity_pct']} %"],
        ["Wind Speed",   f"{data['wind_speed_ms']} m/s"],
        ["Visibility",   f"{data['visibility_m']} m" if data['visibility_m'] != 'N/A' else "N/A"],
        ["Condition",    data["description"]],
    ]

    col_w = [W * 0.42, W * 0.58]
    tbl   = Table(table_data, colWidths=col_w)
    tbl.setStyle(TableStyle([
        # Header row
        ("BACKGROUND",   (0, 0), (-1, 0),  colors.HexColor("#1a73e8")),
        ("TEXTCOLOR",    (0, 0), (-1, 0),  colors.white),
        ("FONTNAME",     (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0),  11),
        ("ALIGN",        (0, 0), (-1, 0),  "CENTER"),
        # Body rows
        ("FONTNAME",     (0, 1), (0, -1),  "Helvetica-Bold"),
        ("FONTSIZE",     (0, 1), (-1, -1), 10),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [colors.HexColor("#f8f9fa"), colors.white]),
        ("ALIGN",        (1, 1), (1, -1),  "CENTER"),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 8),
        ("LEFTPADDING",  (0, 0), (-1, -1), 12),
        ("GRID",         (0, 0), (-1, -1), 0.5, colors.HexColor("#dadce0")),
        ("ROUNDEDCORNERS", [4], ),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 22))

    # ── News Headlines ────────────────────
    story.append(HRFlowable(width=W, thickness=1,
                             color=colors.HexColor("#dadce0"), spaceAfter=12))
    story.append(Paragraph(
        "Latest Weather Headlines",
        _style("Heading2", fontSize=15, textColor=colors.HexColor("#1a73e8"), spaceAfter=10)
    ))
    for i, hl in enumerate(headlines, 1):
        story.append(Paragraph(
            f"<b>{i}.</b>  {hl}",
            _style("Normal", fontSize=10, leading=16,
                   textColor=colors.HexColor("#202124"), spaceAfter=6)
        ))

    story.append(Spacer(1, 18))

    # ── Footer note ───────────────────────
    story.append(HRFlowable(width=W, thickness=0.5,
                             color=colors.HexColor("#dadce0"), spaceAfter=8))
    story.append(Paragraph(
        "Data sourced from OpenWeatherMap API  •  Weather Report App",
        _style("Normal", fontSize=8, textColor=colors.grey, alignment=1)
    ))

    doc.build(story)
    print(f"  ✔ PDF report saved → {path}")
    return path

# ──────────────────────────────────────────
#  DISPLAY HELPERS
# ──────────────────────────────────────────

def print_weather(data: dict) -> None:
    bar = "─" * 44
    print(f"\n  {bar}")
    print(f"  📍 {data['city']}, {data['country']}")
    print(f"  🕐 {data['timestamp']}")
    print(f"  {bar}")
    print(f"  🌡  Temperature : {data['temperature_c']} °C  (feels {data['feels_like_c']} °C)")
    print(f"  💧 Humidity    : {data['humidity_pct']} %")
    print(f"  🌬  Wind Speed  : {data['wind_speed_ms']} m/s")
    vis = f"{data['visibility_m']} m" if data['visibility_m'] != 'N/A' else 'N/A'
    print(f"  👁  Visibility  : {vis}")
    print(f"  ☁  Condition   : {data['description']}")
    print(f"  {bar}\n")


def print_history(history: list[dict]) -> None:
    if not history:
        print("\n  No search history yet.\n")
        return
    print(f"\n  {'#':<4} {'Timestamp':<22} {'City':<18} {'Temp':>6}  {'Hum':>5}  Condition")
    print("  " + "─" * 70)
    for i, row in enumerate(history[-10:], 1):   # show last 10
        print(
            f"  {i:<4} {row['timestamp']:<22} {row['city']:<18} "
            f"{row['temperature_c']:>5}°C  {row['humidity_pct']:>4}%  {row['description']}"
        )
    print()

# ──────────────────────────────────────────
#  MAIN MENU
# ──────────────────────────────────────────

def main():
    print("\n" + "═" * 50)
    print("   🌤   Weather Report Application")
    print("═" * 50)

    if API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        print("\n  ⚠️  No API key set!")
        print("  1. Sign up free at https://openweathermap.org/api")
        print("  2. Copy your key into API_KEY at the top of this file.\n")

    while True:
        print("  [1] Search weather for a city")
        print("  [2] View search history")
        print("  [3] Exit")
        choice = input("\n  Choose an option (1-3): ").strip()

        if choice == "1":
            city = input("  Enter city name: ").strip()
            if not city:
                print("  City name cannot be empty.\n")
                continue

            print(f"\n  Fetching weather for '{city}'…")
            data      = fetch_weather(city)
            headlines = generate_headlines(data)

            print_weather(data)

            print("  Headlines:")
            for i, h in enumerate(headlines, 1):
                print(f"    {i}. {h}")
            print()

            save_to_csv(data)
            generate_pdf(data, headlines)
            print()

        elif choice == "2":
            history = load_history()
            print_history(history)

        elif choice == "3":
            print("\n  Goodbye! ☀️\n")
            break

        else:
            print("  Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
