#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Person:
    def __init__(self):
        self.firstname = "Antoine"
        self.lastname = "De Caunes"
        self.age = 52

une_personne = Person()
une_autre_personne = Person()

print(une_personne.firstname)
print(une_autre_personne.firstname)

une_personne.firstname = "Emma"

print(une_personne.firstname)
print(une_autre_personne.firstname)


# In[32]:


from functools import total_ordering


@total_ordering
class Compte:
    """
    Compte bancaire
    Attribut : 
        - solde
    Methodes:
        - depot(self, montant) ajoute le montant au solde
        - retrait(self, montant) retire le montant au solde
    """
    def __init__(self, solde_init):
        self.solde = solde_init
        
    def retrait(self, montant):
        self.solde -= montant

    def depot(self, montant):
        self.solde += montant
        
    def __lt__(self, other):
        return self.solde < other.solde
        
    def __eq_(self, other):
        return self.solde == other.solde
        
    def __add__(self, other):
        """
            Si other est un compte retourner un compter dont le solde
            est la somme des deux
            Si other est un int ou float retourner un self après avoir fait
            un dépot
        """
        return Compte(self.solde + other.solde)

    def __repr__(self):
        return f"Compte solde: {self.solde}"


class Person:
    """
    Ajouter méthode transfert qui prend un montant de notre compte
    et l'ajoute dans le compte d'une autre personne
    """
    def __init__(self, firstname_init, lastname_init="De Caunes", solde_init=3000):
        self.firstname = firstname_init
        self.lastname = lastname_init
        self.age = 52
        self.compte = Compte(solde_init)

    def dire_bonjour(self, lng="FR"):
        if lng == "FR":
            print(f"Bonjour je m'appelle {self.firstname} {self.lastname}")
        elif lng == "EN":
            print(f"Hello my name is {self.firstname} {self.lastname}")
        elif lng == "RU":
            print(f"Privet menya zovut {self.firstname} {self.lastname}")
        
    def transfert(self, autre_personne, montant):
        self.compte.retrait(montant)
        autre_personne.compte.depot(montant)
        
        
une_personne = Person("Antoine")
une_autre_personne = Person("Emma")
un_etranger = Person("Gerard", "Depardieu")

une_personne.dire_bonjour()
une_personne.age = 53
une_autre_personne.dire_bonjour(lng="EN")
un_etranger.dire_bonjour("RU")

# del une_personne 

une_personne.transfert(une_autre_personne, 500)
print([une_personne.compte, une_personne.compte, une_personne.compte])

print(une_personne.compte <= une_autre_personne.compte)

print(une_personne.compte + une_autre_personne.compte)


# In[14]:


liste_soldes = [42, 45, 65, 24]
liste_personnes = [Person("toto"), Person("tata")]
liste_personnes = [Person("toto", solde_init=solde) for solde in liste_soldes]
liste_personnes[0].dire_bonjour()


# In[20]:


print()


# In[21]:


print

