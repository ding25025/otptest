import pyotp
import time
import qrcode

totp = pyotp.TOTP('base32secret3232')

# OTP_CODE=totp.now() # => '492039'

uri=pyotp.totp.TOTP('base32secret3232').provisioning_uri('user@example.com', issuer_name='YUTINGWU')
 
qrcode.make(uri).save("qr.png")

# verifying the code
while True:
  print(totp.verify(input(("Enter the Code : "))))
  break

# OTP verified for current time
# totp.verify(OTP_CODE) # => True
# print(totp.verify(OTP_CODE))

# totp.verify(OTP_CODE) # => False
# print(totp.verify(OTP_CODE))

#otpauth://totp/ACME%20Co:john.doe@email.com?secret=HXDMVJECJJWSRB3HWIZR4IFUGFTMXBOZ&issuer=ACME%20Co&algorithm=SHA1&digits=6&period=30