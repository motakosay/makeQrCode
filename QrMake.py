import qrcode
img = qrcode.make('Hello_World')
type(img)  # qrcode.image.pil.PilImage
img.save("/content/QRcode_1.jpg")
