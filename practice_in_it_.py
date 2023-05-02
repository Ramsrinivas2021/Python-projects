class laptop():
    def __init__(self,lap_company,lap_ram,lap_processor,lap_price):
        self.a = lap_company
        self.b = lap_ram
        self.c = lap_processor
        self.d = lap_price
            
    def lap_details(self):
        print("lap_company:",self.a)
        print("lap_ram:",self.b)
        print("lap_processor:",self.c)
        print("lap_price:",self.d)

lpc =input("Enter lap_company: ")
lpr =input("Enter lap_ram: ")
lpp =input("Enter lap_procesor: ")
lppr =input("Enter lap_pricr: ")
lap_obj = laptop(lpc,lpr,lpp,lppr)
# lap_obj = laptop("dell",'4gb','i7',80000)
lap_obj.lap_details()
answer = input(("Do you want enter details again:(y/n)"))
if answer == 'y':
    lap_obj.lap_details()
else :
    print("thanks for your time")
