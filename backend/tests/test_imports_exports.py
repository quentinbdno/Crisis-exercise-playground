from imports_exports.services import validate_scenario_yaml


def test_validate_scenario_yaml_requires_name():
    _, errors = validate_scenario_yaml("stimuli: []")
    assert "Missing scenario name" in errors


def test_validate_scenario_yaml_accepts_minimal_scenario():
    data, errors = validate_scenario_yaml("name: Demo\nstimuli: []")
    assert errors == []
    assert data["name"] == "Demo"
