import os


def generate_folder(name: str = "qrcode_img") -> str:
    if not os.path.exists(name):
        os.makedirs(name)
        print(f"Dossier '{name}' créé avec succès.")
    else:
        print(f"Dossier '{name}' existe déjà.")
    return name
