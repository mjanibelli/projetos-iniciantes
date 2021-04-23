import platform

import info_pc_modulo

print(" Informações do PC ".center(31, "="))

if platform.system():
    info_pc_modulo.mostrar_info()
else:
    print("Não foi possível definir seu sistema!")
