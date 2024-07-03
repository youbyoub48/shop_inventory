import json

from os.path import exists

if exists("inventory.json"):
    with open("inventory.json","r") as f:
        products = json.load(f)

else:
    products = {}

if exists("log.json"):
    with open("log.json","r") as f:
        log = json.load(f)

else:
    log = []


def register_product(products:dict,log:list,id:str,name:str,price:float):
    if products.get(id,-1) != -1:
        print("the product already exist")
        return False
    
    products[id] = [name,0,price] #[Name of the product,number of products in stock,price of the product]
    save(products,log)
    return True

def add_product(products:dict,log:list,id:str):
    if products.get(id,-1) == -1:
        print("the product do not exist please register the product before")
        return False
    
    products[id][1] = products[id][1]+1
    log.append(["+", id, products[id][0], products[id][2]])
    save(products,log)
    return True

def remove_product(products:dict,log:list,id:str):
    if products.get(id,-1) == -1:
        print("the product do not exist please register the product before")
        return False
    
    if products[id][1] <= 0:
        print("you can't go under 0 you have surely forgot to add this product")
        return False
    
    products[id][1] = products[id][1]-1
    log.append(["-", id, products[id][0], products[id][2]])
    save(products,log)
    return True

def delete_product(products:dict,log:list,id:str):
    if products.get(id,-1) == -1:
        print("the product do not exist please register the product before")
        return False
    
    products.pop(id)
    save(products,log)
    return True

def list_product(products:dict):
    for element in products:
        print(f"{products[element][0]} : {products[element][1]} {products[element][2]} {element}")

def save(products:dict,log:list):
    with open("inventory.json","w") as f:
        json.dump(products,f,indent=4)
    
    with open("log.json","w") as f:
        json.dump(log,f,indent=4)


if __name__ == "__main__":
    remove_product(products,log,"1234")