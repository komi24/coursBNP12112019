def dire_bonjour(name, age=42, lng="FR"):
    """
        Affiche "Bonjour, je m'appelle {name}. J'ai {age} ans"
        Dans une langue FR (argument par défaut) / EN / PT / ES
        
        :param name: Nom de la personne qui dit bonjour
        :param age: (optionel, par def 42) Nom de la personne 
            qui dit bonjour
        :param lng: Langue utilisée pour saluer
        :return: None
    """
    if lng == "FR":
        print(f"Bonjour, je m'appelle {name}. J'ai {age} ans.")
    if lng == "EN":
        print(f"Hello, my name is {name}. I am {age}.")
    if lng == "PT":
        print(f"Bom dia, me chamo {name}. Tenho {age}.")
    if lng == "ES":
        print(f"Hola, me llamo {name}. Tengo {age}.")
      
if __name__ == "__main__":
    dire_bonjour("Martin", lng="ES")