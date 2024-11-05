import qrcode

features = qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data('https://www.youtube.com/@IITMadrasBSDegreeProgramme')
features.make(fit=True)
generate_image = features.make_image(fill_color="black",background_color="white")
generate_image.save('IITM BS')
generate_image.save('qrcodeimage.png')
