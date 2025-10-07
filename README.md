# itis_dio_cane

Timetable storage system for ITIS Don Morosini Ferentino.

## Overview

This repository provides a JSON-based timetable storage system for ITIS Don Morosini Ferentino, allowing per-class timetables to be stored and managed since the school doesn't provide them officially.

## Files

- `timetable_schema.json` - JSON Schema defining the structure of timetable data
- `timetable.json` - Sample timetable data for classes
- `validate_timetable.py` - Python script to validate timetable against schema

## Timetable Structure

The timetable is organized as follows:

```json
{
  "school": {
    "name": "ITIS Don Morosini",
    "location": "Ferentino",
    "year": "2023-2024"
  },
  "classes": [
    {
      "class_id": "1A",
      "section": "Informatica",
      "year": 1,
      "timetable": {
        "Monday": [...],
        "Tuesday": [...],
        ...
      }
    }
  ]
}
```

Each day contains an array of lessons with:
- `period` - Period number
- `start_time` - Start time (HH:MM)
- `end_time` - End time (HH:MM)
- `subject` - Subject name
- `teacher` - Teacher name (optional)
- `room` - Room/classroom number (optional)

## Usage

1. Edit `timetable.json` to add or modify class timetables
2. Add new classes by adding objects to the `classes` array
3. Each class should have a complete weekly schedule

## Adding a New Class

To add a new class, add a new object to the `classes` array:

```json
{
  "class_id": "2B",
  "section": "Informatica",
  "year": 2,
  "timetable": {
    "Monday": [...],
    "Tuesday": [...],
    "Wednesday": [...],
    "Thursday": [...],
    "Friday": [...]
  }
}
```

## Validation

The timetable data can be validated against the JSON Schema in `timetable_schema.json` using any JSON Schema validator.

A Python validation script is provided for convenience:

```bash
# Install jsonschema (first time only)
pip install jsonschema

# Run validation
python3 validate_timetable.py
```