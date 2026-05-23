import csv
import io
import zipfile

import yaml


def validate_scenario_yaml(raw_text):
    data = yaml.safe_load(raw_text) or {}
    errors = []
    if "name" not in data:
        errors.append("Missing scenario name")
    if not isinstance(data.get("stimuli", []), list):
        errors.append("stimuli must be a list")
    return data, errors


def read_scenario_zip(file_obj):
    with zipfile.ZipFile(file_obj) as archive:
        if "scenario.yaml" not in archive.namelist():
            return None, ["scenario.yaml is required"]
        raw = archive.read("scenario.yaml").decode("utf-8")
        return validate_scenario_yaml(raw)


def scenario_to_csv(stimuli):
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["planned_time_seconds", "sender", "recipient", "type", "channel", "subject", "body"])
    for stimulus in stimuli:
        writer.writerow([
            stimulus.planned_time_seconds,
            stimulus.sender_label,
            stimulus.recipient_label,
            stimulus.stimulus_type,
            stimulus.delivery_channel,
            stimulus.subject,
            stimulus.body,
        ])
    return buffer.getvalue()
