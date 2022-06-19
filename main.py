from classes import *

# Loon uue kooli
Kool = Kool()
Kool.adding_nimi()

# Loon listid
all_õpetajas_list = []
all_õpilased_list = []

# Loon 5 uut õpetajat
print("Loon õpetajad...")

for i in range(5):
    õpetaja = õpetaja()
    õpetaja.naming_õpetajas()
    Kool.adding_õpetaja(õpetaja)
    all_õpetajas_list.append(õpetaja)

# Loon 10 uut õpilast
print("Loon õpilased...")

for i in range(10):
    õpilane = õpilane()
    õpilane.naming_õpilane()
    all_õpilased_list.append(õpilane)

# Loon teise kooli
Kool2 = Kool()
Kool2.adding_nimi()

# Kõigi õpilaste lisamine esimesse kooli ja teisse kooli
for i in all_õpilased_list:
    Kool.registering_õpilane_2kool(i)

for i in all_õpilased_list:
    Kool2.registering_õpilane_2kool(i)