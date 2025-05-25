---
title: Device Tester
nav_order: 1
parent: Platinen
---

# Device Tester PCB

<table>
  <tr><th>Top</th><th>Bottom</th></tr>
  <tr>
    <td><img src="device_test/device_test-3D_top.png?dummy={{ site.data['hash'] }}" alt="top" /></td>
    <td><img src="device_test/device_test-3D_bottom.png?dummy={{ site.data['hash'] }}" alt="bottom" /></td>
  </tr>
</table>

Die `Device Test` Platine enthält alle wichtigen Schnittstellen um die Bus- oder Device-Platinen zu testen.
Sie enthält zwei Bus Stecker um sich an einem Bus-Master oder Bus-Device anzustecken. Weiters verfügt es einen Device Stecker um ein Device anzustecken.
Über zwei USB-C Stecker kann die Platine an einem Computer angesteckt werden.

Es befinden sich auch Jumper auf der Platine um ein Computer Module 4 (Raspberry Pi) zu flashen.

| Spannung | bereitgestellt durch |
| -------- | -------------------- |
|      +5V |                USB-C |
|     +12V |     Schraubverbinder |

## Daten

- [Schaltplan](device_test/device_test-schematic.pdf)
- [BOM](device_test/device_test-bom.html)
- [iBOM](device_test/device_test-ibom.html)
- [JLCPCB fabrication & stencil](device_test/JLCPCB/device_test-_JLCPCB_compress.zip)
- [JLCPCB Bom](device_test/JLCPCB/device_test_bom_jlc.csv)
- [JLCPCB Pick&Place](device_test/JLCPCB/device_test_cpl_jlc.csv)

## Gefundene Probleme in v0.1

- [X] 12V Klemme treffen direkt auf ETH-Port -> auf andere Seite vom USB-C Port wechseln
- [X] 5V von USB-C oder Bus-PCB? -> Jumper
- [X] Möglichkeit vorsehen damit das Modul eingeschoben werden kann (nicht alles Bestücken?)
