# lancement du projet

Avoir docker et docker-compose  

lancer la commande: `docker-compose up -d`  

url: `localhost:5000`  


# Question Poo

## Utilisation de visibilité publique (lien dans votre code) + définition
Il n'y a pas vraiment de notion de privé, protéger en public en python cependant celui-ci est implémenté avec des conventions  
[Fichier word.py ligne 8 (self.allPasswords())](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/word.py#L8)  
C'est un attribut ou une méthode accessible à l'exterieur de la class  

## Utilisation de visibilité privée (lien dans votre code) + définition
[Fichier date.py ligne 5 (self.__date = date)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/date.py#L5)  
C'est un attribut ou une méthode accessible seulement à l'intérieur de sa class  

## Utilisation de visibilité protégée (lien dans votre code) + définition
[Fichier L33t.py ligne 5 (self._word = _word)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/l33t.py#L5)  
C'est un attribut ou une méthode accessible à l'intérieur de sa class ou de ses class enfantes

## Utilisation du polymorphisme (lien dans votre code) + définition
[initialisation méthode fichier word.py ligne 77 (def getAllIndex(self):)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/word.py#L77)  
[Surcharge de la méthode Fichier L33t.py ligne 54(## surcharge méthode)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/l33t.py#L55)  
C'est la surcharge d'une méthode. C'est à dire la modification de se signature (nom de la méthode, les paramètres ou le type de retour)  

## Utilisation de l'encapsulation (lien dans votre code) + définition
Disponnible dans plusieurs fichier  
[word.py ligne 8 (self.allPasswords())](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/word.py#L8)  
[L33t.py ligne 5 (self._word = _word)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/l33t.py#L5)  
[date.py ligne 5 (self.__date = date)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/date.py#L5)  
C'est l'utilisation des visibilités publics, privés et protégés

## Utilisation de composition (lien dans votre code) + définition
[Fichier merge.py ligne 32 (date = Date(date_object))](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/merge.py#L32)  
C'est l'appel à une class et l'utilisation de celle-ci dans une autre class

## Utilisation de l'héritage (lien dans votre code) + définition
[Fichier L33t.py ligne 3 (class L33t(Word):)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/l33t.py#L3)  
L'héritage est un design pattern permmettant de créer un hiérarchie entre les class. les classes enfant héritent des propriétés de la classe parente tout en ajoutant ou en modifiant une propriété / méthode

## Utilisation d'interface (lien dans votre code) + définition
Ce n'est pas possible de faire une interface en python donc je ne l'ai pas réalisé  
Une interface permet de créer un plan qui sera obligatoire et intégrer directement dans la class qui l'implemente  

## Utilisation de méthodes et attributs d'objets (lien dans votre code) + définition
[Fichier word.py ligne 34 (def toUpperCase(self, withoutAccent=None):)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/word.py#L34)  
C'est une méthode qui a accès aux méthodes et attribues de la class. Cependant il est obligatoire d'avoir instancié un objet de cette class pour pouvoir l'utiliser

## Utilisation de méthodes et attributs statiques (lien dans votre code) + définition
[Fichier word.py ligne 22 (@staticmethod)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/word.py#L22)  
C'est une méthode qui n'a accès a aucune méthode ou attribue de la class. Cette méthode peut-etre utilisé sans avoir besoin d'instancier un objet de cette class

## Utilisation de méthodes et attributs de classe (lien dans votre code) + définition
[Fichier word.py ligne 28 (@classmethod)](https://github.com/AlexandreBecavin/passwordGuesser/blob/master/app/word.py#L28)  
C'est une méthode qui a accès aux méthodes et attribues de la class. Cette méthode peut-etre utilisé sans avoir besoin d'instancier un objet de cette class