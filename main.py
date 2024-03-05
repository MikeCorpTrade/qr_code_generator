import qrcode
import os
from generate_folder import generate_folder


def generate_qr_code(link):
    # Création de l'objet QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Ajout du lien
    qr.add_data(link)
    qr.make(fit=True)

    # Création de l'image QR code
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def main():
    # Demander à l'utilisateur de saisir le lien
    link = input("Entrez le lien pour générer le QR code: ")

    # Générer le QR code
    qr_code = generate_qr_code(link)

    # Enregistrer l'image
    folder_name = generate_folder()
    file_name = input("Entrez le nom de fichier pour enregistrer le QR code : ")
    file_path = os.path.join(folder_name, file_name)
    qr_code.save(f"{file_path}.png")

    print("QR code généré avec succès !")


if __name__ == "__main__":
    main()
