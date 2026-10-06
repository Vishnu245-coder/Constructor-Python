class Bank:
    Bank_name="ABC Bank"
    Bank_Loc="Kukatplally"
    Branch_Code="ABC001"
    def __init__(self,Account_No,Customer_Name,Balance,Account_Type,Mobile_No):
        self.Account_No=Account_No
        self.Customer_Name=Customer_Name
        self.Balance=Balance
        self.Account_Type=Account_Type
        self.Mobile_No=Mobile_No

    def Display(self):
        print("Bank Name : ",Bank.Bank_name)
        print("Bank Location : ",Bank.Bank_Loc)
        print("Branch Code : ",self.Branch_Code)
        print("Account No : ",self.Account_No)
        print("Customer Name = ",self.Customer_Name)
        print("Current Balance : ",self.Balance)
        print("Account Type : ",self.Account_Type)
        print("Mobile Number : ",self.Mobile_No)

print("----------  Customer 1  -----------")
t1=Bank("2453 3456 4356","Vikas","1,00,000","Savings Account","1234567890")
t1.Display()
print()
print("----------  Customer 2  -----------")
t2=Bank("2345 7896 3423","Shankar","50,000","Current Account","9834622353")
t2.Display()


# ----------  Customer 1  -----------
# Bank Name :  ABC Bank
# Bank Location : Kukatpally
# Branch Code :  ABC001
# Account No :  2453 3456 4356
# Customer Name =  Vikas
# Current Balance :  1,00,000
# Account Type :  Savings Account
# Mobile Number :  1234567890

# ----------  Customer 2  -----------
# Bank Name :  ABC Bank
# Bank Location : Kukatpally
# Branch Code :  ABC001
# Account No :  2345 7896 3423
# Customer Name =  Shankar
# Current Balance :  50,000
# Account Type :  Current Account
# Mobile Number :  9834622353

# Example 2  

class Restaurent:
    Res_name="ABC Restaurent"
    City="Hyderabad"
    def __init__(self,Customer_Name,Item_Name,Item_Price,Quantity,Total_Amount):
        self.Customer_Name=Customer_Name
        self.Item_Name=Item_Name
        self.Item_Price=Item_Price
        self.Quantity=Quantity
        self.Total_Amount=Total_Amount
    def Display(self):
        print("Restaurent Name : ",Restaurent.Res_name)
        print("Restaurent Location : ",Restaurent.City)
        print("Customer Name : ",self.Customer_Name)
        print("Item Name : ",self.Item_Name)
        print("Item Price : ",self.Item_Price)
        print("Quantity : ",self.Quantity)
        print("Total Amount : ",self.Total_Amount)

print()
print("------------  Order 1  -------------")
t1=Restaurent("Vikas","Chicken Dum Biryani","₹250",2,"₹500")  
t1.Display()          
print()

print("------------  Order 2  -------------")
t2=Restaurent("Shankar","Mutton Keema Biryani","₹420",1,"₹420")
t2.Display()

# ------------  Order 1  -------------
# Restaurent Name :  ABC Restaurent
# Restaurent Location :  Hyderabad
# Customer Name :  Vikas
# Item Name :  Chicken Dum Biryani
# Item Price :  ₹250
# Quantity :  2
# Total Amount :  ₹500

# ------------  Order 2  -------------
# Restaurent Name :  ABC Restaurent
# Restaurent Location :  Hyderabad
# Customer Name :  Shankar
# Item Name :  Mutton Keema Biryani
# Item Price :  ₹420
# Quantity :  1
# Total Amount :  ₹420


# Example 3


class LibraryManagement:
    Lib_Name="ABC Library"
    Location="Hyderabad"
    def __init__(self, member_name, member_id, book_name, issue_date):
        self.member_name=member_name
        self.member_id=member_id
        self.book_name=book_name
        self.issue_date=issue_date

    def Display(self):
        print("Library Name : ",LibraryManagement.Lib_Name)
        print("Location : ",LibraryManagement.Location)
        print("Member Name : ", self.member_name)
        print("Member ID  : ",self.member_id)
        print("Book Name : ", self.book_name)
        print("Issued Date : ",self.issue_date)

print()
print("---------  Member 1  ------------")
t1=LibraryManagement("Vikas",1001,"Python Crash Course","23-09-2026")  
t1.Display()

print()
print("---------  Member 2  ------------")
t2=LibraryManagement("Shankar",1002,"Hands-On Machine Learning","23-09-2026")
t2.Display()


# ---------  Member 1  ------------
# Library Name :  ABC Library
# Location :  Hyderabad
# Member Name :  Vikas
# Member ID  :  1001
# Book Name :  Python Crash Course
# Issued Date :  23-09-2026            

# ---------  Member 2  ------------
# Library Name :  ABC Library
# Location :  Hyderabad
# Member Name :  Shankar
# Member ID  :  1002
# Book Name :  Hands-On Machine Learning
# Issued Date :  23-09-2026