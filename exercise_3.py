contact_list = {
    "Anadoo": "0900", 
    "Terkaa": "0901", 
    "Aondongu": "0902", 
    "Sewuese": "0903"
} 

print(contact_list)
print(contact_list.get("Anadoo"))
print(contact_list["Anadoo"])  
contact_list["Anadoo"] = "2014"

print(contact_list)

contact_list.update({"Anadoo": "0900"}) 
print(contact_list) 

contact_list.update({"Selumun": "0905"})

print(contact_list)
#del contact_list["Selumun"]
#contact_list.pop("Selumun") 
print(contact_list)
#contact_list.pop("Tinubu")
print(contact_list.items) 
print(contact_list) 
contact_list.popitem() 

print(contact_list) 
print("")
new = contact_list.copy()
#new.popitem()
print(new) 
