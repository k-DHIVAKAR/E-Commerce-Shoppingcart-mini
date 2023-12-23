class shopping_cart():
    list_of_products={'shirts':[3,599],'shorts':[10,800],'t-shirt':[20,400],'shoe':[0,750]}
    def __init__(self,name,phone_no,email,address):
        self.name=name
        self.phone_no=phone_no
        self.email=email
        self.address=address
        self.cart={}

    @classmethod
    def display_products(cls):
        print("Product Available in the shop are:")
        print("Item","Quantity","Price")
        print()
        for product in cls.list_of_products:
            print(product,cls.list_of_products[product][0],cls.list_of_products[product][1])
        print()

    def display_details(self):
        print("Your details are:")
        print()
        print(f'Name : {self.name}')
        print(f'Phone number: {self.phone_no}')
        print(f'Emial-ID: {self.email}')
        print(f'Address: {self.address}') 
        if self.cart=={}:
            print("Your Cart is Empy")
            print()
        else:
            print()
            print("Products in Your cart are:") 
            total=0
            for product in self.cart:
                print(product,self.cart[product],self.list_of_products[product][1]*self.cart[product])
                total+=self.list_of_products[product][1]*self.cart[product]
            print("Total:" , total)
            print()
    def add_products(self):
        self.display_products()
        product=input("Enter the Product Name:")
        if product in shopping_cart.list_of_products:
            qty=int(input("Enter the Quantity:"))
            if shopping_cart.list_of_products[product][0]>=qty:
                if product in self.cart:
                    self.cart[product]+=qty
                else:
                    self.cart[product]=qty
                shopping_cart.list_of_products[product][0]-=qty
                print()
                print("...Product Added Successfully...")
                print()
            else:
                print(f'Quantity is not available! only {shopping_cart.list_of_products[product][0]} {product} are left')
        else:
            print("***This is not availble in the shop***")
    def remove_product(self):
        if self.cart=={}:
            print("Your cart is empty! Cannot remove any product")
        else:
            product=input("Enter the product name:")
            if product in self.cart:
                qty=int(input("Enter the Quantity:"))
                if self.cart[product]>=qty:
                    self.cart[product]-=qty
                    shopping_cart.list_of_products[product][0]+=qty
                    print()
                    print("...Product removed successfully...")
                    print()
                    if self.cart[product]==0:
                        self.cart.pop(product)
                else:
                    print()
                    print(f'Cannot remove! {self.cart[product] } {product} is present in cart')
                    print()
            else:
                print()
                print("...This Product is not present in your cart...")
                print()
    def main(self):
        print('---------------WELCOME-----------------')
        print()
        while True:
            option=int(input('''Press
1. To Display all the products available in the shop.
2. To Display Your Details.
3. To Add a product into the cart.
4. To Remove the product from the cart.
5. T0 Exit.

Enter Your option: ''') )
          
            if option==1:
                self.display_products()
            elif option ==2:
                self.display_details()
            elif option==3:
                self.add_products()
            elif option==4:
                self.remove_product()
            elif option==5:
                print("Thankyou For Your Shopping!,Have a nice Day")
                break
            else:
                print("Invalid option! Please choose again")
             
c1=shopping_cart("Dhivakar",7603822936,"dhivakarhiva1903@gmail.com","Thiruvaiyaru")
c1.main()
