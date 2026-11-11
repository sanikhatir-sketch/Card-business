import qrcode
from qrcode.constants import ERROR_CORRECT_H

cv_url = input("Paste your CV public link: ").strip()
if not cv_url.startswith(("https://", "http://")):
    raise SystemExit("Please enter a valid URL starting with https:// or http://")

qr = qrcode.QRCode(
    version=None,
    error_correction=ERROR_CORRECT_H,
    box_size=12,
    border=2
)
qr.add_data(cv_url)
qr.make(fit=True)
qr.make_image(fill_color="#102a4c", back_color="white").save("qr.png")
print("Updated qr.png successfully.")
