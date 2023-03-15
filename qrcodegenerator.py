import qrcode
import image

qr = qrcode.QRCode(
    version=15, #15 means the version of the qrcode high the number the bigger the code image
    box_size=10, #size of the box where qr code will be displayed
    border=5 #it is tehe white part of the image
     
)

data = "https://www.youtube.com/watch?v=xtIr8k4eC7o"

qr.add_data(data)
qr.make(fit = True)
img = qr.make.image(fill="black",back_color="white")
img.save("test.png")