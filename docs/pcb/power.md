---
title: Power PCB
nav_order: 3
parent: Platinen
---

# Power PCB

<table>
  <tr><th>Top</th><th>Bottom</th></tr>
  <tr>
    <td><img src="power/power-3D_top.png?dummy={{ site.data['hash'] }}" alt="top" /></td>
    <td><img src="power/power-3D_bottom.png?dummy={{ site.data['hash'] }}" alt="bottom" /></td>
  </tr>
</table>

Dieses Modul stellt die benötigten Spannungen (+5V und +12V) für den Bus zur Verfügung.
Diese Spannungen und Ströme können mit 2 INA226 gemessen werden.

| Spannung |   INA226 Adresse |
| -------- | ---------------- |
|     +12V | 0b1000001 (0x41) |
|      +5V | 0b1000000 (0x40) |

Die +12V Versorgungsspannung wird über eine XT60 Buchse ermöglicht. Diese Spannung wird direkt an den Bus weiter gegeben. Somit ist die +12V Bus-Spannung direkt abhängig vom Eingang des Modules.

| Spannung | Spannungsbereich |
| -------- | ---------------- |
|     +12V |     11.8 - 14.6V |

Die +5V Versorgungsspannung wird von den +12V über einen Buck-Converter erzeugt. Diese ist somit stabil auf +5V geregelt, jedoch auf 3A begrenzt.

## Daten

- [Schaltplan](power/power-schematic.pdf)
- [BOM](power/power-bom.html)
- [iBOM](power/power-ibom.html)
- [JLCPCB fabrication & stencil](power/JLCPCB/power-_JLCPCB_compress.zip)
- [JLCPCB Bom](power/JLCPCB/power_bom_jlc.csv)
- [JLCPCB Pick&Place](power/JLCPCB/power_cpl_jlc.csv)
