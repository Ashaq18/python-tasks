import pyqrcode
url="https://youtu.be/CvHzWF_iTLo?si=ooQxn4uhydhVQLlO"
k=pyqrcode.create(url)
k.svg('qr.svg',scale=10)