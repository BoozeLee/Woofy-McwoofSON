"""
Test: Ensure ADR action registry and code registry are in sync.

- Parses the ADR index table in adr/README.md for all documented actions/decisions.
- Loads the action registry from src/action_registry.py.
- Verifies each ADR-documented action exists in the registry, and vice versa.

To run:
    pytest tests/test_adr_registry_sync.py
"""

import re
import os
import importlib.util

ADR_README = os.path.join(os.path.dirname(__file__), "..", "adr", "README.md")
ACTION_REGISTRY = os.path.join(
    os.path.dirname(__file__), "..", "src", "action_registry.py"
)


def parse_adr_actions():
    """Parse ADR index table for action/decision titles."""
    with open(ADR_README, "r", encoding="utf-8") as f:
        lines = f.readlines()
    # Find start of ADR table
    start = None
    for idx, line in enumerate(lines):
        if line.strip().startswith("| ADR #"):
            start = idx + 2
            break
    if start is None:
        raise AssertionError("ADR index table not found in adr/README.md")
    actions = []
    for line in lines[start:]:
        if not line.strip() or not line.startswith("|"):
            break
        parts = [x.strip() for x in line.strip("| \n").split("|")]
        if len(parts) > 1:
            actions.append(parts[1])
    return set(actions)


def get_registry_actions():
    """Import action_registry.py and return set of action names."""
    spec = importlib.util.spec_from_file_location("action_registry", ACTION_REGISTRY)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Convention: registry is a dict or list called ACTIONS or ACTION_REGISTRY
    if hasattr(module, "ACTION_REGISTRY"):
        registry = getattr(module, "ACTION_REGISTRY")
    elif hasattr(module, "ACTIONS"):
        registry = getattr(module, "ACTIONS")
    else:
        raise AssertionError(
            "No ACTIONS or ACTION_REGISTRY found in src/action_registry.py"
        )
    if isinstance(registry, dict):
        return set(registry.keys())
    if isinstance(registry, list):
        return set(registry)
    raise AssertionError("ACTION_REGISTRY/ACTIONS is not a dict or list")


def test_adr_and_registry_actions_are_in_sync():
    adr_actions = parse_adr_actions()
    registry_actions = get_registry_actions()
    missing_in_registry = adr_actions - registry_actions
    missing_in_adr = registry_actions - adr_actions
    msg = ""
    if missing_in_registry:
        msg += f"Actions in ADR index but missing from action registry: {missing_in_registry}\n"
    if missing_in_adr:
        msg += (
            f"Actions in action registry but missing from ADR index: {missing_in_adr}\n"
        )
    assert not missing_in_registry and not missing_in_adr, msg
