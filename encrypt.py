class Encrypt:
    def __init__  (self):
        self.send = ""
        self.res = []



    def sender (self):
        self.send = input("Ente The Data: ")
        self.res =  [ ord (i) +2 for i in self.send ]
        print ("Encrypted Data: " , "" .join (chr (i) for i in self.res))
       

#
class Decrypt (Encrypt):
    def receiver (self):
       decrypted_data = "". join(chr (i - 2) for i in self.res)
       print ("Decrypted Data: " , decrypted_data)


obj = Decrypt()
obj.sender()
obj.receiver()
