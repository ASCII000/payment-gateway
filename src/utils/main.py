"""
Module contains utils functions without categorie
"""

import json
from datetime import datetime, timezone

def now_utc_iso() -> str:
    """
    Obtem a data e hora atual em UTC no formato ISO
    """

    return datetime.now(timezone.utc).isoformat()

def empty_json_str() -> str:
    """
    Obtem um json vazio
    """
    return json.dumps({})