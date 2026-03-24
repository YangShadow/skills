#!/usr/bin/env python3
"""
Fetch Federal Reserve and economic data.
Uses FRED API (St. Louis Fed) for economic indicators.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, Optional

try:
    import requests
except ImportError:
    requests = None


# FRED API endpoint (free tier available)
FRED_BASE_URL = "https://api.stlouisfed.org/fred"

# Key economic indicators
INDICATORS = {
    "DFF": "Federal Funds Rate",
    "CPIAUCSL": "Consumer Price Index",
    "PPIACO": "Producer Price Index",
    "UNRATE": "Unemployment Rate",
    "PAYEMS": "Nonfarm Payrolls",
    "VIXCLS": "VIX Volatility Index",
    "DTWEXBGS": "Trade Weighted US Dollar Index",
    "DGS10": "10-Year Treasury Rate",
    "DGS2": "2-Year Treasury Rate",
}


def fetch_fred_data(series_id: str, api_key: Optional[str] = None) -> Dict:
    """Fetch data from FRED API."""
    if requests is None:
        return {}

    try:
        url = f"{FRED_BASE_URL}/series/observations"
        params = {
            "series_id": series_id,
            "sort_order": "desc",
            "limit": 2,
            "file_type": "json",
        }
        if api_key:
            params["api_key"] = api_key

        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        observations = data.get("observations", [])
        if len(observations) >= 2:
            current = observations[0]
            previous = observations[1]

            try:
                current_val = float(current["value"])
                previous_val = float(previous["value"])
                change = current_val - previous_val
            except (ValueError, TypeError):
                current_val = current["value"]
                previous_val = previous["value"]
                change = None

            return {
                "series_id": series_id,
                "title": INDICATORS.get(series_id, series_id),
                "current_value": current_val,
                "previous_value": previous_val,
                "change": change,
                "date": current["date"],
                "previous_date": previous["date"],
            }
    except Exception as e:
        print(f"Error fetching {series_id}: {e}")

    return {}


def fetch_all_indicators(api_key: Optional[str] = None) -> Dict[str, Dict]:
    """Fetch all key economic indicators."""
    results = {}

    for series_id in INDICATORS:
        data = fetch_fred_data(series_id, api_key)
        if data:
            results[series_id] = data

    return results


def format_indicator_value(indicator: str, value: float) -> str:
    """Format indicator value based on type."""
    if indicator in ["DGS10", "DGS2", "DFF", "UNRATE"]:
        return f"{value:.2f}%"
    elif indicator == "VIXCLS":
        return f"{value:.2f}"
    elif indicator == "DTWEXBGS":
        return f"{value:.2f}"
    else:
        return f"{value:,.2f}"


if __name__ == "__main__":
    # Fetch without API key (some endpoints work without)
    data = fetch_all_indicators()

    # Format for display
    formatted = {}
    for series_id, info in data.items():
        formatted[series_id] = {
            "name": info["title"],
            "value": format_indicator_value(series_id, info["current_value"]),
            "change": info["change"],
            "date": info["date"],
        }

    print(json.dumps(formatted, ensure_ascii=False, indent=2))
