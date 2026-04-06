#!/usr/bin/env python3
import csv
import json
import argparse
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Convert CSV files to JSON format")
    parser.add_argument("input_file", help="Input CSV file path")
    parser.add_argument(
        "--output", "-o", help="Output JSON file path (default: stdout)"
    )
    parser.add_argument(
        "--pretty", "-p", action="store_true", help="Output formatted/indented JSON"
    )
    return parser.parse_args()


def read_csv(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as f:
            content = f.read()
            if not content.strip():
                print("Error: File is empty", file=sys.stderr)
                sys.exit(1)
            f.seek(0)
            reader = csv.DictReader(f)
            if reader.fieldnames is None:
                print("Error: No header row found in CSV file", file=sys.stderr)
                sys.exit(1)
            rows = []
            try:
                for row in reader:
                    rows.append(row)
            except csv.Error as e:
                print(f"Error: Malformed CSV - {e}", file=sys.stderr)
                sys.exit(1)
            return rows
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied: {file_path}", file=sys.stderr)
        sys.exit(1)


def write_json(data, output_path, pretty=False):
    indent = 2 if pretty else None
    json_output = json.dumps(data, indent=indent, ensure_ascii=False)

    if output_path:
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(json_output)
                f.write("\n")
            return output_path
        except PermissionError:
            print(f"Error: Permission denied: {output_path}", file=sys.stderr)
            sys.exit(1)
        except IOError as e:
            print(f"Error: Cannot write to {output_path}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(json_output)
        return "stdout"


def main():
    args = parse_args()
    rows = read_csv(args.input_file)
    output_path = write_json(rows, args.output, args.pretty)

    location = output_path if args.output else "stdout"
    print(
        f"Success: Converted {len(rows)} row(s) to JSON ({location})", file=sys.stdout
    )


if __name__ == "__main__":
    main()
