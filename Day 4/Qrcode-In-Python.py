import qrcode
u=input('Enter valid URL: ')
i=qrcode.make(u)
i.show()