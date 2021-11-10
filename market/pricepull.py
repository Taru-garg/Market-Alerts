import json
import requests
from .config import API_BASE_ENDPOINT


def _get_market_name(market_user_passed: str) -> str:
    return market_user_passed.lower() + "inr"


def _fetch_all_tickers() -> str:
    return (requests.get(API_BASE_ENDPOINT)).text


def _extract_market_info(market_name: str, tickers: dict) -> float:
    return float(tickers[market_name]["last"])


def pull(market_user_passed: str) -> float:
    return _extract_market_info(
        _get_market_name(market_user_passed), json.loads(_fetch_all_tickers())
    )
