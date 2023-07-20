##Ejercicio 2
#Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:
##  Añadir a cualquier persona, indicando nombre y después teléfono
##Buscar el teléfono de una persona
## 
##Ampliación:
##Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:
##Introduce un nombre: Pep
####Resultados:
######Pepe 659331013
#######Pepe Martín 633743551

agenda ={
    "Pepe":"659331013",
    "Pepe Martin" : "633743551"
}

def show_menu():
    print("Menu:")
    print("1. Add New Contact")
    print("2. Search Contacts")
    print("0. Exit")

def add_contact(name, phone):
    agenda.update({name : phone})

def search_contacts(name):
    contacts = []
    
    for key, value in agenda.items():
        if name in key:
            contacts.append((key, value))

    for key, value in contacts:
        print(key, value)

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the new contact: ")
            phone = input("Now enter a phone number: ")
            add_contact(name,phone)
        elif choice == "2":
            search = input("Enter a name to search: ")
            search_contacts(search)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid option, please select a valid one :)")
