"""Módulo para econtrar e retornar informações do sistema."""
import platform


def mostrar_info():
    """Recebe as informações do sistema e as printa no terminal."""
    processador = platform.processor()

    if not processador:
        processador = "Processador não encontrado."

    print(f"- Sistema Operacional: {platform.system()}")
    print(f"- Plataforma do sistema: {platform.platform()}")
    print(f"- Versão do sistema: {platform.version()}")
    print(f"- Processador: {processador}")
    print(f"- Arquitetura do processador: {platform.architecture()[0]}")

    if platform.system() == "Windows":
        print(f"- Edição do Windows: {platform.win32_edition()}")
