# csv2json

A simple Python CLI tool to convert CSV files to JSON format.

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Usage

### Basic usage (output to stdout)

```bash
python csv2json.py input.csv
```

### Output to a file

```bash
python csv2json.py input.csv --output output.json
```

### Pretty-printed JSON output

```bash
python csv2json.py input.csv --pretty
```

### Combined flags

```bash
python csv2json.py input.csv --output output.json --pretty
```

## Examples

### Example CSV (test.csv)

```csv
name,age,email,city
John Doe,28,john@example.com,New York
Jane Smith,34,jane@example.com,Los Angeles
```

### Example Output

```bash
$ python csv2json.py test.csv --pretty
[
  {
    "name": "John Doe",
    "age": "28",
    "email": "john@example.com",
    "city": "New York"
  },
  {
    "name": "Jane Smith",
    "age": "34",
    "email": "jane@example.com",
    "city": "Los Angeles"
  }
]
Success: Converted 2 row(s) to JSON (stdout)
```

## Error Handling

The tool handles various error cases:

- File not found
- Empty files
- CSV files without headers
- Malformed CSV data
- Permission errors

All errors are printed to stderr with descriptive messages.

## Testing

A sample file `test.csv` is included. Run:

```bash
python csv2json.py test.csv --pretty
```

Or redirect to a file:

```bash
python csv2json.py test.csv --output output.json
```