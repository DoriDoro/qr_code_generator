import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

data_of_qr_code = 'Do not forget to subscribe'


# create a simple QR Code:
image_of_qr_code = qrcode.make(data_of_qr_code)

image_of_qr_code.save('/ update your path /qrcode.png')


# create a QR Code in red:
qr_code_red = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr_code_red.add_data(data_of_qr_code)

qr_code_red.make(fit=True)

image_qr_red = qr_code_red.make_image(fill_color = 'red', back_color = 'white')

image_qr_red.save('/ update your path /qrcode_red.png')


# get data written out of existing QR Code:
decode_qr = Image.open('/Users/mac/Desktop/Projects/QR_code/qrcode_red.png')

result = decode(decode_qr)

print(result)
