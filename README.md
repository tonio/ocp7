-[_Parcours Open Classrooms_](|https://openclassrooms.com/fr/projects/creez-grandpy-bot-le-papy-robot| "Créez GrandPy Bot, le papy-robot")-

# [PyDev] Projet 7

## _Note_

_La dernière version à jour de ce document est disponible sur [github](https://github.com/freezed/ocp7/blob/master/README.md)._

---
## Créez GrandPy Bot, le papy-robot

### Cahier des charges

#### Fonctionnalités

*   Interactions en AJAX : question envoyée en appuyant sur entrée : la réponse s'affiche sans recharger la page.
*   Vous utiliserez l'[API de Google Maps][gmaps] ([leafletJS][leaflet], [OSM][osm]?) et celle de [Media Wiki][mediawiki]
*   Rien n'est sauvegardé (page rechagée == historique perdu)
*   [option] Plusieurs réponses différentes peuvent être faites

#### Parcours utilisateur

L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie. Il arrive devant une page contenant les éléments suivants :

*   header : logo et phrase d'accroche
*   zone centrale : zone vide (qui servira à afficher le dialogue) et formulaire pour envoyer une question.
*   footer : votre prénom & nom, lien vers le repo et autres

L'utilisateur tape dans le champ de formulaire puis appuie sur la touche `entrée` :

> "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"

Le message s'affiche dans la zone du dessus qui affiche tous les messages échangés. Une icône tourne pour indiquer que GrandPy est en train de réfléchir.

Puis un nouveau message apparaît :

>"Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris."

En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.

GrandPy envoie un nouveau message :

> "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse. [[En savoir plus sur Wikipedia](https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis)]"

### Étapes

1. Découpez votre projet en étapes et sous-étapes en suivant une méthodologie de projet agile que vous adapterez à vos besoins.
2. Créez un nouveau projet avec [Flask][flask], un framework Python très léger.
3. Adoptez une approche Test Driven Development: commencez par écrire vos tests, puis votre code et refactorisez.
4. L'interface doit être responsive et consultable sur mobile  ([Bootstrap][bootstrap])
5. Un parser de killer. vous découperez la phrase en mots que vous analyserez ensuite pour ne garder que les mots-clés (une adresse par exemple). _Petite astuce_. une excellente [base de stop words][stopword] en français
6. Afficher les résultats de la recherche Google Maps. Utilisez un mock pour tester cette nouvelle fonctionnalité.
7. Récupérer les informations de Wikipedia correspondant à l’endroit recherché et afficher les premières lignes.
8. Puis mettez en ligne votre belle application en utilisant [Heroku][heroku].

### Livrables

- [Document texte expliquant la démarche][approach]
    * difficultés rencontrées / solutions trouvées
    * lien _Github_
    * lien du _site déployé_ pour utiliser votre projet en production
    * format pdf n'éxcédant pas 2 pages A4
    * rédigé en anglais ou français
- Code source [dépôt sur _Github_][readme]
- Tableau agile [Project table sur github][kaban]

### Contraintes

*   Interface responsive
*   Test Driven Development
*   Code intégralement écrit en anglais : fonctions, variables, commentaires, ...
*   Utilisation d'AJAX pour l'envoi des questions et l'affichage des réponses (une seule langue au choix, anglais ou français)
*   Tests utilisant des mocks pour les API

[approach]: https://github.com/freezed/ocp7/blob/master/doc/approach.md
[doc]: https://github.com/freezed/ocp7/blob/master/doc/documentation.md#documentation "Project documentation"
[gmaps]: https://cloud.google.com/maps-platform/?hl=fr "API Google Maps"
[kaban]: https://github.com/freezed/ocp7/projects/1
[leaflet]: https://leafletjs.com/reference-1.3.2.html "LeafletJS API"
[mediawiki]: https://www.mediawiki.org/wiki/API:Main_page/fr
[osm]: https://wiki.openstreetmap.org/wiki/API_v0.6 "OSM API"
[readme]: https://github.com/freezed/ocp7/blob/master/README.md
[stopword]: https://github.com/6/stopwords-json/blob/master/dist/fr.json
[heroku]: https://devcenter.heroku.com/articles/getting-started-with-python
[flask]: https://www.palletsprojects.com/p/flask/ "Flask is a Python web development framework based on the Werkzeug, Jinja, MarkupSafe and itsdangerous pallets libraries."
[bootstrap]: https://github.com/twbs/bootstrap#bootstrap "Sleek, intuitive, and powerful front-end framework for faster and easier web development"
