import pdb

from tabulate import tabulate
from typing import List, TypedDict

class TabulatePrintOptions(TypedDict):
  filter: list
  format: str
  headers: bool
  select: list

def tabulate_print(records: List[dict], **kwargs: TabulatePrintOptions):
  show_header = kwargs.get('headers')
  filter = kwargs.get('filter') or []
  format = kwargs.get('format') or 'plain'
  select = kwargs.get('select') or []

  headers = []
  rows = []
  for record in records:
    build_header = show_header and len(headers) == 0

    row = []
    for key, val in record.items():
      # If exclude list is provided, check if key is excluded
      if key in filter:
        continue
      
      # If include list is provided, check if key is included
      if len(select) > 0 and key not in select:
        continue

      if build_header:
        headers.append(key)

      row.append(val)

    rows.append(row)

  print(tabulate(rows, headers=headers, tablefmt=format))