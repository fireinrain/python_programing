#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

class Property:
    def __init__(self,square_feet='',beds='',baths='',**kwargs):
        super().__init__(**kwargs)
        self.square_feet=square_feet
        self.num_bedrooms=beds
        self.num_baths=baths

    def dispaly(self):
        print("property details")
        print("================")
        print("square footage:{}".format(self.square_feet))
        print("bedrooms:{}".format(self.num_bedrooms))
        print("bathrooms:{}".format(self.num_baths))
        print()


    def prompt_init():
        return dict(square_feet=input("enter the square feet:"),beds=input("enter number of bedrooms:"),
                    baths=input("enter number of baths:"))
    prompt_init=staticmethod(prompt_init)


#验证输入
def get_valid_input(input_string,valid_options):
    input_string+="({})".format(",".join(valid_options))
    response=input(input_string)
    while response.lower() not in valid_options:
        response=input(input_string)
    return response

class Apartment(Property):
    valid_laundries=("coin","ensuite","none")
    valid_balconies=("yes","no","solarium")

    def __init__(self,balcony='',laundry='',**kwargs):
        super().__init__(**kwargs)
        self.balcony=balcony
        self.laundry=laundry

    def prompt_init():
        parent_init=Property.prompt_init()
        laundry=get_valid_input("what laundry facilities does the property have",Apartment.valid_laundries)
        balcony=get_valid_input("does the property hava a balcony",Apartment.valid_balconies)

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)

    def dispaly(self):
        super().display()
        print("apartment display")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

        parent_init=Property.promt_init()
        laundry=''
        while laundry.lower() not in Apartment.valid_laundries:
            laundry=input("what laundry facilities does the property have?({})".format(
                ",".join(Apartment.valid_laundries)
            ))
        balcony=''
        while balcony.lower() not in Apartment.valid_balconies:
            balcony = input("does the property have a balcony?({})".format(
                ",".join(Apartment.valid_balconies)
            ))





