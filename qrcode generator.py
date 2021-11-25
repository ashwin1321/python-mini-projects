import pyqrcode
import png
from pyqrcode import QRCode


#string which represents the QR code
user_input = input("Enter your desired content: ")


#Generate QR code
gen = pyqrcode.create(user_input)

# Create and save the svg file "myqr.svg"
gen.svg("myqr.svg", scale = 8)

#create and save the png file naming "myqr.png"
gen.png('myqr.png', scale =6)