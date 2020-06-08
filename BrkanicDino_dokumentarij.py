# Dokumentarij je aplikacija za ispis i unos novih studenata 
# na kolegiju Razvoj poslovnih aplikacija
# za brisanje: https://note.nkmk.me/en/python-list-clear-pop-remove-del/

import random 

class DokumentarijModel:
    def __init__(self):
        self._names 

    @property
    def names(self):
        return self._names
    
    @names.setter
    def item_type (self, new_name):
        self._names = new_name
    
    def create_name(self):
        name 
        return name 

class DokumentarijView:
    def display_title_bar(self):    
        print("\t****************************************************")
        print("\t***  Dokumentarij - Razvoj poslovnih aplikacija  ***")
        print("\t****************************************************")
        
   
    def get_user_choice(self):
        # Let users know what they can do.
        print("\n[1] Pogledaj listu studenata.")
        print("[2] Dodaj novog studenta.")
        print("[x] Izlaz.")
        
        return input("Što želite napraviti u dokumentariju?")
        
    def show_names(self):
        # Shows the names of everyone who is already in the list.
        print("\nOvo je popis studenata na kolegiju Razvoj poslovnih aplikacija 2019/2020:\n")
        for name in self.names:
            print(name.title())
            
    def get_new_name(self):
        # Asks the user for a new name, and stores the name if we don't already
        #  know about this person.
        new_name = input("\nUnesite ime studenta: ")
        if new_name in self.names:
            print("\n{} je već upisan/a u dokumentariju!".format(new_name.title()))
        else:
            self.names.append(new_name)
            print("\nDobrodošao/la {}!\n".format(new_name.title()))

    ### MAIN PROGRAM ###

    # Set up a loop where users can choose what they'd like to do.
   
class DokumentarijController: 
    def play(self):
        self.names = []

        choice = ''
        self.display_title_bar()
        while choice != 'x':    
            
            choice = self.get_user_choice()
            
            # Respond to the user's choice.
            self.display_title_bar()
            if choice == '1':
                self.show_names()
            elif choice == '2':
                self.get_new_name()
            elif choice == 'x':
                print("\nHvala na pregledu/uređivanju dokumentarija. Pozdrav.")
            else:
                print("\nGreška - napravite hvatanje izuzetaka sami za vježbu.\n")
                
if __name__ == "__main__":
    game = Dokumentarij()
    game.play()