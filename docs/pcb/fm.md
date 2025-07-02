---
title: FM PCB
nav_order: 5
parent: Platinen
---

# FM PCB

<table>
  <tr><th>Top</th><th>Bottom</th></tr>
  <tr>
    <td><img src="fm/fm-3D_top.png?dummy={{ site.data['hash'] }}" alt="top" /></td>
    <td><img src="fm/fm-3D_bottom.png?dummy={{ site.data['hash'] }}" alt="bottom" /></td>
  </tr>
</table>

Das `FM` Modul beherbergt einen FM Chip für das 2m oder 70cm Band.

| Spannung |                          benötigter Strom |
| -------- | ----------------------------------------- |
|      +5V |                                   max. 1A |
|     +12V | max. 1A (SA818) via buck converter for 5V |

## Daten

- [Schaltplan](fm/fm-schematic.pdf)
- [BOM](fm/fm-bom.html)
- [iBOM](fm/fm-ibom.html)
- [JLCPCB fabrication & stencil](fm/JLCPCB/fm-_JLCPCB_compress.zip)
- [JLCPCB Bom](fm/JLCPCB/fm_bom_jlc.csv)
- [JLCPCB Pick&Place](fm/JLCPCB/fm_cpl_jlc.csv)
