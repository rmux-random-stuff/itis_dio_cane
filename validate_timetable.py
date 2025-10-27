#!/usr/bin/env python3
"""
Validate timetable.json against the JSON schema.
Requires: pip install jsonschema
"""

import json
import sys

try:
    import jsonschema
except ImportError:
    print("Error: jsonschema module not found.")
    print("Please install it with: pip install jsonschema")
    sys.exit(1)

def validate_timetable():
    """Validate the timetable against the schema."""
    try:
        # Load schema
        with open('timetable_schema.json', 'r', encoding='utf-8') as f:
            schema = json.load(f)
        
        # Load timetable
        with open('timetable.json', 'r', encoding='utf-8') as f:
            timetable = json.load(f)
        
        # Validate
        jsonschema.validate(instance=timetable, schema=schema)
        
        print("✓ Timetable is valid!")
        return True
        
    except jsonschema.exceptions.ValidationError as e:
        print(f"✗ Validation error: {e.message}")
        print(f"  Path: {' -> '.join(str(p) for p in e.path)}")
        return False
    except FileNotFoundError as e:
        print(f"✗ File not found: {e.filename}")
        return False
    except json.JSONDecodeError as e:
        print(f"✗ JSON parse error: {e}")
        return False

if __name__ == '__main__':
    success = validate_timetable()
    sys.exit(0 if success else 1)
