import pyqrcode
def qr():
    s  = " Hey guys, it's me Leela  Saud"
    d = pyqrcode.create(s)
    d.png("qrcode.png", scale=6)
    print("code is executed properly")
if __name__ == "__main__":
    qr()