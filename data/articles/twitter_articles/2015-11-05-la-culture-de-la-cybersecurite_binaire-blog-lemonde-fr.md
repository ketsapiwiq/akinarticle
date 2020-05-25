---
title: "La culture de la cybersécurité"
url: http://binaire.blog.lemonde.fr/2015/11/05/la-culture-de-la-cybersecurite/
keywords: systèmes,quil,monde,sdm,exemple,culture,sécurité,système,faille,cest,cybersécurité,code
---
Dans le cadre des « Entretiens autour de l'informatique », [Serge Abiteboul](http://abiteboul.com) et [Claire Mathieu](http://www.di.ens.fr/ClaireMathieu.html) ont rencontré Stanislas de Maupeou, Directeur du secteur Conseil en sécurité chez Thalès. Stanislas de Maupeou parle à Binaire de failles de logiciels et de cybersécurité.

**Failles, attaques et exploits... et certification**

B : À quoi sont dûs les problèmes de sécurité informatique ?\
SdM : Le code utilisé est globalement de mauvaise qualité et, de ce fait, il existe des failles qui ouvrent la porte à des attaques. Le plus souvent, ce sont des failles involontaires, qui existent parce que le code a été écrit de façon hâtive. Il peut y avoir aussi des failles intentionnelles, quelqu'un mettant volontairement un piège dans le code.

Il y a des sociétés, notamment aux USA, dont le travail est de trouver les failles dans le logiciel. C'est toute une économie souterraine : trouver une faille et la vendre. Quand on trouve une faille, on y associe un « exploit » (\*), un code d'attaque qui va exploiter la faille. On peut vendre un exploit à un éditeur de logiciels (pour qu'il comble la faille) ou à des criminels. Si une telle vente est interdite par la loi en France, cela se fait dans le monde anglo-saxon. Pour ma part, si je trouve une faille dans un logiciel, je préviens l'éditeur en disant : « on vous donne trois mois pour le corriger, et si ce n'est pas fait, on prévient le public ».

C'est pour pallier au risque de faille qu'on met en place des processus de certification de code. Mais développer un code sans faille, ou avec moins de failles, cela peut avoir un coût faramineux. On ne peut pas repenser tout un système d'exploitation, et même dans des systèmes très stratégiques, il est impensable de réécrire tout le code. Ça coûterait trop cher.

B : Comment certifiez-vous le code ?\
SdM : Il y a différentes méthodes. J'ai des laboratoires de certification. Nous n'écrivons pas le code. Nous l'évaluons selon un schéma de certification, suivant une échelle de sûreté qui va de 1 à 7. En France, la certification est gérée par l'ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information). Le commanditaire dit : « Je voudrais que vous certifiez cette puce », et l'ANSSI répond « Adressez vous à l'un des laboratoires suivants qui ont été agréés». Sur l'échelle, le 1 signifie « J'ai une confiance minimum », et le 7 signifie « j'ai une confiance absolue ». Le niveau « évaluation assurance niveau 7 » ne peut être obtenu que par des méthodes formelles, de preuve de sécurité. Par exemple, nous avons certifié au niveau 7 un élément de code Java pour Gemalto. Il y a peu de spécialistes des méthodes formelles dans le monde, un seul dans mon équipe. Dans le monde bancaire, on se contente des niveaux 2 et 3. On fait des tests en laboratoire, on sollicite le code, on regarde la consommation électrique pour voir si c'est normal. On fait ça avec du laser, de l'optique, il y a tout un tas d'équipements qui permettent de s'assurer que le code « ne fuit pas ». Pour la certification de hardware, le contrôle se faire à un niveau très bas. On a le plan des puces, le composant, et on sait le découper en couches pour retrouver le silicium et faire des comparaisons.

B : Le code lui-même est-il à votre disposition?\
SdM : Parfois oui, si on vise à développer la confiance dans les applications. C'est par exemple le cas pour l'estampille « visa » sur la carte bancaire qui donne confiance au commerçant. Dans d'autres contextes, on n'a pas accès au code. Par exemple, on nous demande de faire des tests d'intrusion. Il s'agit de passer les barrières de sécurité. Le but est de prendre le contrôle d'un système, d'une machine, par exemple avec une requête SQL bien ficelée.

B : Cela aide si le logiciel est libre ?\
SdM : Le fait qu'un logiciel soit libre n'est pas un argument de sécurité. Par exemple, dans la librairie SSL de Debian, il y avait eu une modification de quelque chose de totalement anodin en apparence, mais du coup le générateur de nombres aléatoires pour la librairie SSL n'avait plus rien d'aléatoire ; on n'a découvert cette erreur  que deux ans plus tard. Pendant deux ans tous les systèmes qui reposaient sur SSL avaient des clés faciles à prévoir. Ce n'est pas parce qu'un logiciel est libre qu'il est sûr ! Par contre, s'il est libre, qu'il est beaucoup utilisé, et qu'il a une faille, il y a de fortes chances que quelqu'un la trouve et que cela conduise à sa correction. Cela dit, pour la sécurité, un bon code, qu'il soit libre ou pas, c'est un code audité !

B : Est-ce que les méthodes formelles vont se développer ?\
SdM : On a besoin aujourd'hui de méthodes formelles plus pour la fiabilité du composant que pour la sécurité. On fait de la gestion de risque, pas de la sécurité absolue qui n'existe pas. Vérifier les systèmes, c'est le Graal de la sécurité. On peut acheter un pare-feu au niveau 3, mais, transposer ça à tout un système, on n'y arrive pas. Notre palliatif, c'est une homologation de sécurité : on prend un système, on définit des objectifs de sécurité pour ce système (par exemple, que toute personne qui y accède doive être authentifiée), et on vérifie ces objectifs. On sait qu'il y aura toujours des trous, des risques résiduels, mais au moins, le système satisfait des règles conformes avec certains objectifs de sécurité. C'est une approche non déterministe, elle est floue, et on accepte qu'il y ait un risque résiduel.

Un problème c'est qu'on ne sait pas modéliser le risque. Je sais dire qu'un boulon casse avec probabilité 1%, cela a un sens, mais je ne sais pas dire quelle est la probabilité d'une attaque dans les 10 jours. Comme on ne peut pas modéliser la malveillance, on ne sait pas vraiment faire l'évaluation de la sécurité d'un système avec une approche rationnelle.

**Les métiers de la cybersécurité**

B : Quel est le profil des gens qui travaillent dans votre laboratoire ?\
SdM : Ce sont des passionnés. Ils viennent plutôt d'écoles spécifiquement d'informatique que d'écoles d'ingénieur généralistes comme les Mines, ENSTA, ou Supélec, où les élèves sont moins passionnés par l'informatique.

B : Comment en êtes vous arrivé à vous intéresser à la cybersécurité ?\
SdM : À l'origine j'étais militaire, et pas du tout en lien avec l'informatique. Étudiant, je n'avais pas accroché au Fortran ! Et puis, quand on fait une carrière militaire, après une quinzaine d'années, on suit une formation. Il était clair que le système militaire allait avoir de plus en plus d'informatique. J'ai suivi en 1996, un mastère de systèmes d'information à l'ENST avec stage chez Matra, et j'ai adoré. Même si à l'époque, on ne parlait absolument pas de sécurité, j'ai réorienté ma carrière vers le Service central de sécurité et services d'information, un petit service de 30 personnes, qui à l'origine ne servait guère qu'à garder le téléphone rouge du président. À l'époque, un industriel devait donner à l'état un double de sa clé de chiffrement. En 1999, il y a eu un discours de Lionel Jospin à Hourtin, dans lequel il a dit que ce n'était plus viable et qu'il fallait libéraliser la cryptographie, libérer ce marché. À l'époque il fallait déclarer toute clé de plus de 40 bits. Il a demandé qu'on élève le seuil à 128 bits, et c'est grâce à cela que les sites de la SNCF, la FNAC, etc., ont pu se développer. Ce service est devenu une agence nationale, passant de 30 à plus de 400 personnes, l'ANSSI.

Ensuite je suis passé chez Thalès où j'ai eu à manager des informaticiens. Ce n'est pas une population facile à manager. Et puis le domaine évolue très vite ; nous sommes en pleine période de créativité. On a encore plus besoin de management.

B : Qu'est ce qu'un informaticien devrait savoir pour être recruté dans votre domaine ?\
SdM : J'aimerais qu'il connaisse les fondamentaux de la sécurité. J'aimerais qu'il y ait un cours « sécurité » qui fasse partie de la formation et qui ne soit pas optionnel. L'ennemi essaie de gagner des droits, des privilèges. Les fondamentaux de la sécurité, c'est, par exemple, la défense en profondeur, le principe du moindre privilège systématique sur des variables, la conception de codes segmentés, le principe du cloisonnement, les limites sur le temps d'exécution. Le moindre privilège est une notion essentielle. Le but est de tenir compte de la capacité du code à résister à une attaque. Déjà, avoir du code plus propre, de meilleure qualité au sens de la sécurité, avec plus de traçabilité, une meilleure documentation, cela aide aussi. Mais tout cela a un coût. Un code sécurisé, avec des spécifications, de l'évaluation, de la relecture de code, cela coûte 30 à 40% plus cher.

**Etat et cybersécurité**

B : Est-ce que l'ANSSI a un rôle important dans la sécurité informatique ?\
SdM : L'ANSSI a un rôle extrêmement important, pour s'assurer que les produits qui seront utilisés par l'état ou par des opérateurs d'importance vitale (définis par décret, par exemple les télécommunications, les banques, EDF, la SNCF, Areva...) satisfont à des règles. L'ANSSI peut imposer des normes par la loi, garantissant un niveau minimum de qualité ou sécurité sur des éléments critiques, par le biais de décisions comme « Je m'autorise à aller chez vous faire un audit si je le décide. »

B : De quoi a-t-on peur ?\
SdM : La première grande menace que l'État craint est liée à l'espionnage. En effet, l'immense majorité des codes et produits viennent de l'extérieur de la France. Un exemple de régulation : les routeurs Huawei sont interdits dans l'administration française. La deuxième menace, c'est le dysfonctionnement ou la destruction de système. L'État craint les attaques terroristes sur des systèmes industriels. Ces systèmes utilisent aujourd'hui des logiciels standard, et de ce fait, sont exposés à des attaques qui n'existaient pas auparavant. Une des grandes craintes de l'état, c'est la prise de contrôle d'un barrage, d'un avion, etc. C'est déjà arrivé, par exemple, il y a eu le cas du « ver informatique » Stuxnet en Iran, qui a été diffusé dans les centrales nucléaires iraniennes, qui est arrivé jusqu'aux centrifugeuses, qui y a provoqué des dysfonctionnements de la vitesse de la centrifugeuse, cependant que le contrôleur derrière son pupitre ne voyait rien. Avec Stuxnet, les US sont arrivés à casser plusieurs centrifugeuses, d'où des retards du programme nucléaire iranien. Un déni de service sur le système de déclaration de l'impôt fin mai, c'est très ennuyeux mais il n'y a pas de mort. Un déni de service sur le système de protection des trains, les conséquences peuvent être tout à fait dramatiques, d'un autre ordre de gravité.

Il y a aussi une troisième menace, sur la protection de la vie privée. Dans quelle mesure suis-je libre dans un monde qui sait tout de moi ? Dans les grands volumes de données, il y a des informations qui servent à influencer les gens et à leur faire prendre des décisions. C'est une préoccupation sociétale.

B : En quoi le fonctionnement de l'armée en temps de guerre a-t-il été modifié par l'informatique ?\
SdM : L'armée aux États-Unis est beaucoup plus technophile que l'armée française, qui a mis un certain temps à entrer dans ce monde-là. Dans la fin des années 1990, les claviers sans fil étaient interdits, le wifi était interdit, le protocole Internet était interdit. Aujourd'hui, l'armée française en Afghanistan utilise énormément le wifi. Maintenant, il n'y a plus de système d'armes qui n'utilise pas d'informatique.

B : La sécurité est-elle une question franco-française ?\
SdM : Il faut admettre que le monde de la sécurité est très connecté aux services de renseignement, ce qui rend les choses plus difficiles. Pour gérer les problèmes en avionique, on est dans un mode coopératif. Si un modèle pose un problème mécanique, on prévient tout le monde. En revanche, dans le monde de la sécurité informatique, si on trouve une faille, d'abord on commence par se protéger, puis on prévient l'état qui, peut-être, se servira de cette information. Ce sont deux logiques qui s'affrontent, entre la coopération et un monde plus régalien, contrôlé par l'État.

B : Avez vous un dernier mot à ajouter ?\
SdM : Il faudrait développer en France une culture de la « sécurité ». Peu de systèmes échappent aujourd'hui à l'informatique. La sécurité devrait être quelque chose de complètement naturel, pas seulement pour les systèmes critiques. C'est comme si on disait, les bons freins, ce n'est que pour les voitures de sport. La sécurité doit être intégrée à tout.

(\*) Exploit : prononcer exploït, anglicisme inspiré du verbe anglais "to exploit" qui signifie exploiter, lui-même inspiré du français du 15e siècle.

[Signaler ce contenu comme inapproprié](http://www.contact-moderation.com/abuse.asp?origine=LM&language=FR&content_id=blog-2701164)