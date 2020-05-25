---
title: "« Backdoor » dans WhatsApp : le créateur de Signal défend le choix ergonomique"
url: https://www.nextinpact.com/news/102905-backdoor-dans-whatsapp-createur-signal-defend-choix-ergonomique.htm
keywords: léditeur,créateur,manière,savoir,backdoor,protocole,signal,sécurité,dune,whatsapp,clé,défend,choix,bout,ergonomique
---
La polémique autour de WhatsApp ne se calme pas. L'article du Guardian sur une possible porte dérobée a provoqué de nombreuses réactions, où s'entrechoquent sécurité et ergonomie. Pour Open Whisper Systems, créateur du protocole Signal, il n'est cependant pas question d'une « backdoor ».

[L'affaire est complexe](https://www.nextinpact.com/news/102882-la-securite-whatsapp-en-question-porte-derobee-ou-choix-ergonomique.htm), car elle oppose plusieurs visions d'une situation répondant de choix techniques. Commençons par rappeler que WhatsApp utilise le protocole de chiffrement de bout en bout Signal, développé par Open Whisper Systems (OWS). Un processus qui permet de s'assurer, quand les clés sont contrôlées, que l'expéditeur et le destinataire sont bien qui ils prétendent être.

### La clé privée peut changer pour plusieurs raisons

Chaque utilisateur de WhatsApp dispose de deux clés, l'une publique, l'autre privée. La deuxième dépend explicitement du smartphone sur lequel l'application a été installée. Il peut cependant y avoir plusieurs raisons pour que cette clé soit modifiée : un changement de téléphone, de carte SIM, une réinstallation de l'application, etc. Auquel cas, WhatsApp génère une nouvelle clé privée pour l'utilisateur, toujours basée sur les caractéristiques locales de l'appareil.

Ce fonctionnement n'a rien d'unique et est commun à toutes les solutions de messagerie utilisant un chiffrement de bout en bout. On le retrouve ainsi dans Viber, ou encore dans les conversations « secrètes » de Facebook Messenger et Telegram. Cependant, la manière de communiquer à l'utilisateur qu'un changement a eu lieu peut nettement varier.

### Plusieurs manières de gérer les changements de clés

Dans Signal par exemple, application utilisant le protocole du même nom, aucun changement de clé ne peut avoir lieu sans que la personne concernée (expéditeur ou destinataire) ne soit avertie. Non seulement un message informe que le code de sécurité est différent, mais les messages ultérieurs ne sont plus délivrés tant que la nouvelle clé n'a pas été acceptée, à charge à l\'utilisateur de vérifier sa véracité. Et ce qui fait tant réagir autour de WhatsApp, c'est que ces étapes sont absentes par défaut.

La clé peut donc changer sans que personne ne soit au courant, à moins d'aller fouiller dans les options de sécurité pour activer ces notifications. Un constat qui avait fait réagir le chercheur Tobias Boelter de l'université de Berkeley (Californie), qui avait alerté Facebook [en avril 2016](https://tobi.rocks/2016/04/whats-app-retransmission-vulnerability/) du danger. Que se passerait-il en effet si une attaque de l'homme du milieu (MITM) devait réussir, aboutissant à la génération malveillante d'une nouvelle clé ?

### Sécurité contre choix ergonomique

C'est ici que les avis divergent profondément. Pour le chercheur et [The Guardian](https://www.theguardian.com/technology/2017/jan/13/whatsapp-backdoor-allows-snooping-on-encrypted-messages), on peut parler d'une authentique porte dérobée. Pour d'autres, notamment Frederic Jacobs -- qui a travaillé sur le protocole Signal -- une telle idée est « ridicule », le fonctionnement de WhatsApp reposant sur un évident choix ergonomique. Nous indiquions d'ailleurs que le faisceau d'éléments allait dans le sens du toujours très délicat équilibre entre ergonomie et sécurité, au « détriment » de la seconde.

Pour Open Whisper System, qui s'est fendu vendredi soir [d'un long billet de blog](https://whispersystems.org/blog/there-is-no-whatsapp-backdoor/) pour donner sa position, le constat est le même. L'éditeur, en tant que père du protocole Signal, dispose en effet d'un certain poids, qu'il investit dans la défense de WhatsApp.

### WhatsApp ne peut pas savoir qui a activé l\'option

OWS aborde ainsi un élément important : les serveurs de WhatsApp sont conçus de manière à ne jamais savoir qui a activé l'option de notification des changements de clés. En d'autres termes, l'éditeur ignore qui voit réellement qu'une clé a changé. Dès lors, pourquoi WhatsApp prendrait le risque de changer la clé pour d'autres motifs que ceux évoqués, au risque de provoquer un scandale sur la sécurité de son service ?

En outre, OWS insiste sur le fait que l'implémentation faite par WhatsApp rend impossible tout renvoi des messages déjà reçus et lus (double « check » bleu) par le destinataire. Ce qui doit permettre, dans le cas où les serveurs seraient contrôlés par un tiers, de ne pas accéder à l'historique d'une conversation.

Le développeur de Signal l'affirme : la manière dont WhatsApp gère ses clés ne constitue pas une porte dérobée, « c'est la manière dont fonctionne la cryptographie ». Il serait par ailleurs bien délicat de parler de porte dérobée dans la mesure où ce fonctionnement est connu depuis presque un an, quand WhatsApp a activé par défaut le chiffrement de bout en bout pour l'ensemble des utilisateurs -- à condition qu'ils disposent d'une version récente de l'application.

### Un choix « approprié »

La seule question pertinente pour Open Whisper Systems est de savoir si les notifications de changements de clés devraient être bloquantes, comme dans l'application Signal. L'éditeur ne donne pas de réponse absolue, mais estime que WhatsApp a fait un choix « approprié », pour une raison simple : la taille de la base d\'utilisateurs, qui dépasse le milliard. Une volonté de privilégier l'ergonomie. SI WhatsApp ajoutait le blocage des messages en se basant sur l'option de notification, le serveur aurait les moyens de savoir qui l'a activée ou pas. La situation serait alors « pire ».

L'éditeur regrette par ailleurs la manière dont l'histoire a été abordée par The Guardian et s'étonne de ne pas avoir été contactée, alors même que la technologie centrale impliquée est la sienne. Il tente de résumer : « Il y a bien des choses que l'on peut critiquer chez Facebook, mais faire tourner un produit qui a déployé le chiffrement de bout en bout par défaut chez plus d'un milliard de personnes n'est pas l'une d'elles ».

### La grande valse des théories du complot

Si l'article du Guardian a eu un tel écho, c'est également car il s'agit d'un journal anglais et que le contexte au Royaume-Uni est particulier actuellement. Le vote d'une [loi particulièrement musclée](https://www.nextinpact.com/news/102196-le-parlement-britannique-adopte-loi-renseignement-tres-musclee.htm) sur le renseignement a marqué les esprits, car elle autorise notamment la récupération en masse des données de navigation et le piratage distant des ordinateurs par les forces de l'ordre.

Rapidement, autant dans l'article que dans les réactions des autres médias, la question a été posée : et si un gouvernement demandait à WhatsApp de changer la clé d'un utilisateur pour suivre toutes ses conversations futures, une mise en place qui reste techniquement possible ? Une interrogation qui fleurit sur un terrain très propice aux doutes, particulièrement depuis les révélations d'Edward Snowden.

Mais si l'on se base sur les informations recueillis jusqu'ici, une telle demande semble avoir peu de risques d'aboutir. WhatsApp a indiqué [dans un communiqué](http://arstechnica.com/security/2017/01/whatsapp-and-friends-take-umbrage-at-report-its-crypto-is-backdoored/) que des explications poussées sur le chiffrement utilisé sont disponibles sur son site. L'éditeur affirme également être transparent sur les demandes faites par les gouvernements. En outre, s'il est impossible pour les serveurs de savoir qui a activé l'option, le risque de s'apercevoir de la manœuvre est trop important, alors même que le renseignement tâche d'opérer dans l'ombre.

On rappellera finalement que le mieux est d'activer l'option qui se trouve dans Réglages, Compte puis Sécurité. Un encadré jaune apparaîtra alors pour signaler qu'un changement de clé a eu lieu, permettant de poser la question à son contact sur un éventuel changement de smartphone ou une réinstallation de l'application.
