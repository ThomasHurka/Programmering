class Poketmonster:
    def __init__(self, element : str, name : str, health : int, attack : int, defence : int):
        self.name = name 
        self.element = element 
        self.health = health
        self.attack = attack
        self.defence = defence

    def poketbattle(self, target):
        match self.element: 
            case "grass":
                match target.element:
                    case "fire":
                        effect = 0.5
                    case "water":
                        effect = 2
                    case _:
                        effect = 1 
            case "fire":
                match target.element:
                    case "water":
                        effect = 0.5
                    case "grass":
                        effect = 2 
                    case _: 
                        effect = 1 
            case "electric": 
                match target.element: 
                    case "water":
                        effect = 2
                    case _:
                        effect = 1 
            case "water":
                match target.element:
                    case "fire":
                        effect = 2
                    case "grass":
                        effect = 0.5
                    case _:
                        effect = 1 
            
        target.health -= 50 * (self.attack/target.defence) * effect

        return target.health

    def __str__(self):
        return self.health

    
        

pookit1 = Poketmonster("fire", "pookit1", 24, 5, 40)
pookit2 = Poketmonster("water", "pookit2", 20, 10, 3)



while True:
    print(pookit2.health)           
    print(pookit1.poketbattle(pookit2))     
    
    
