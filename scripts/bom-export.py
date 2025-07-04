#!/bin/env python3

import argparse
import csv
from dataclasses import dataclass
from inventree import company
from inventree.api import InvenTreeAPI
from inventree.part import Part, PartCategory, BomItem

parser = argparse.ArgumentParser(prog="KiCad Bom export to InvenTree")
parser.add_argument("--csv_file", required=True)
parser.add_argument("--name", required=True)
parser.add_argument("--version", required=True)
parser.add_argument("--pcb_image", required=True)
parser.add_argument("--assembly_image", required=True)
args = parser.parse_args()


# must define connection settings in environment variables!
# INVENTREE_API_HOST
#    INVENTREE_API_USERNAME
#    INVENTREE_API_PASSWORD
# OR
#    INVENTREE_API_TOKEN
api = InvenTreeAPI()


@dataclass(slots=True)
class BuildPart:
    reference: str
    qty: int
    lcsc: str | None
    mouser: str | None
    inventree_part: Part | None = None

    def compare_and_fetch(self, supplier_part: company.SupplierPart) -> bool:
        matching = (self.lcsc and self.lcsc == supplier_part.SKU) or (
            self.mouser and self.mouser == supplier_part.SKU
        )
        if matching:
            self.inventree_part = Part(api, pk=supplier_part.part)
        return matching


parts: list[BuildPart] = []

with open(args.csv_file, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        parts.append(
            BuildPart(
                row["References"],
                row["Quantity Per PCB"],
                row["LCSC"] if len(row["LCSC"]) > 0 else None,
                row["MOUSER"] if len(row["MOUSER"]) > 0 else None,
            )
        )

# parts matching
supplier_parts = company.SupplierPart.list(api)

for part in parts:
    for supplier_part in supplier_parts:
        if part.compare_and_fetch(supplier_part):
            break

# check all parts if something is missing
for part in parts:
    if not (part.lcsc is None and part.mouser is None):
        assert part.inventree_part is not None, f"{part}"

pcb_cat = PartCategory(api, 54)
pcb_part = Part.create(
    api,
    {
        "category": pcb_cat.pk,
        "name": f"{args.name} PCB",
        "revision": args.version,
        "component": True,
    },
)
response = pcb_part.uploadImage(args.pcb_image)
assert response is not None

pcb_cat = PartCategory(api, 2)
assembly_part = Part.create(
    api,
    {
        "category": pcb_cat.pk,
        "name": f"{args.name} Module",
        "revision": args.version,
        "component": True,
        "assembly": True,
        "trackable": True,
    },
)
response = assembly_part.uploadImage(args.assembly_image)
assert response is not None

bom_item = BomItem.create(
    api,
    {
        "part": assembly_part.pk,
        "sub_part": pcb_part.pk,
        "reference": "",
        "quantity": 1,
    },
)

for part in parts:
    if part.inventree_part is not None:
        bom_item = BomItem.create(
            api,
            {
                "part": assembly_part.pk,
                "sub_part": part.inventree_part.pk,
                "reference": part.reference,
                "quantity": part.qty,
            },
        )
