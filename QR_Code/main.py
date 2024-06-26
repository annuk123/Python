import qrcode as qr

# Generate the QR code
img = qr.make("https://bio.link/annukumalu")

# Save the generated QR code as an image file
img.save("Annu_biolink.png")

