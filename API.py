import json

from os.path import exists

if exists("inventory.json"):
    with open("inventory.json","r") as f:
        products = json.load(f)

else:
    products = {}


def register_product(products:dict,id:str,name:str):
    if products.get(id,-1) != -1:
        print("the product already exist")
        return False
    
    products[id] = [name,0]
    save(products)
    return True

def add_product(products:dict,id:str):
    if products.get(id,-1) == -1:
        print("the product do not exist please register the product before")
        return False
    
    products[id][1] = products[id][1]+1
    save(products)
    return True

def remove_product(products,id):
    if products.get(id,-1) == -1:
        print("the product do not exist please register the product before")
        return False
    
    if products[id][1] <= 0:
        print("you can't go under 0 you have surely forgot to add this product")
        return False
    
    products[id][1] = products[id][1]-1
    save(products)
    return True

def delete_product(products,id):
    if products.get(id,-1) == -1:
        print("the product do not exist please register the product before")
        return False
    
    products.pop(id)
    save(products)
    return True

def list_product(products):
    for element in products:
        print(f"{products[element][0]} : {products[element][1]} {element}")

def save(products):
    with open("inventory.json","w") as f:
        json.dump(products,f,indent=4)


if __name__ == "__main__":
    remove_product(products,"12345")