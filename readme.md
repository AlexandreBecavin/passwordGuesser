# lancement du projet

Avoir docker et docker-compose

lancer la commande `docker-compose up -d`

aller sur l'url `localhost:5000`


# Question Poo

## Utilisation de visibilité publique (lien dans votre code) + définition
Fichier word.py ligne 8 (self.allPasswords())
C'est un attribut ou une méthode accessible depuis une autre class

## Utilisation de visibilité privée (lien dans votre code) + définition
Fichier date.py ligne 5 (self.__date = date)
C'est un attribut ou une méthode accessible seulement à l'intérieur de sa class

## Utilisation de visibilité protégée (lien dans votre code) + définition
Fichier L33t.py ligne 5 (self._word = _word)
C'est un attribut ou une méthode accessible à l'intérieur de sa class ou ses class enfantes

## Utilisation du polymorphisme (lien dans votre code) + définition
initialisation méthode fichier word.py ligne 76 (def getAllIndex(self):)
Surcharge de la méthode Fichier L33t.py ligne 54(## surcharge méthode)
C'est la surcharge d'une méthode. C'est à dire la modification de se signature (nom de la méthode, les paramètres ou le type de retour)

## Utilisation de l'encapsulation (lien dans votre code) + définition
Disponnible dans plusieurs fichier (L33t.py ligne 5 (self._word = _word), date.py ligne 5 (self.__date = date), word.py ligne 8 (self.allPasswords()))
C'est l'utilisation des visibilités publics, privés et protégés

## Utilisation de composition (lien dans votre code) + définition
Fichier merge.py ligne 32 (date = Date(date_object))
C'est l'appel à une class et l'utilisation de celle-ci dans une autre class

## Utilisation de l'héritage (lien dans votre code) + définition
Fichier L33t.py ligne 3 (class L33t(Word):)
L'héritage est un design pattern permmettant de créer un hiérarchie entre les class. les classes enfant héritent des propriétés de la classe parent, tout en ajoutant ou en modifiant leur propre comportement spécifique.

## Utilisation d'interface (lien dans votre code) + définition
Ce n'est pas possible de faire une interface en python donc je ne l'ai pas réalisé
Une interface permet de créer un plan qui sera obligatoire et intégrer directement dans la class qui l'implemente 

## Utilisation de méthodes et attributs d'objets (lien dans votre code) + définition
Fichier word.py ligne 34 (def toUpperCase(self, withoutAccent=None):)
C'est une méthode qui a accès aux méthodes et attribues de la class. Cependant il est obligatoire d'avoir instancié un objet de cette class pour pouvoir l'utiliser

## Utilisation de méthodes et attributs statiques (lien dans votre code) + définition
Fichier word.py ligne 22 (@staticmethod)
C'est une méthode qui n'a accès a aucune méthode ou attribue de la class. Cette méthode peut-etre utilisé sans avoir besoin d'instancier un objet de cette class

## Utilisation de méthodes et attributs de classe (lien dans votre code) + définition
Fichier word.py ligne 28 (@classmethod)
C'est une méthode qui a accès aux méthodes et attribues de la class. Cette méthode peut-etre utilisé sans avoir besoin d'instancier un objet de cette class