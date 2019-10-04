import pyqrcode
import png

url = pyqrcode.create('http://uca.edu')
#url.svg('uca-url.svg', scale=8)
#url.eps('uca-url.eps', scale=2)

# Create a model of QRCODE
data = pyqrcode.create('http://uca.edu', error='L', version=1, mode='binary')
# Generate PNG image
data.png('files/code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
# Show the image / Save it.
data.show()


