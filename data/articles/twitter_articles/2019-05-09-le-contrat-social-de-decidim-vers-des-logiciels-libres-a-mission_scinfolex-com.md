---
title: "Le Contrat Social de Decidim : vers des logiciels libres « à mission"
url: https://scinfolex.com/2019/05/09/le-contrat-social-de-decidim-vers-des-logiciels-libres-a-mission/
keywords: projet,licence,programme,libres,social,logiciel,plateforme,source,libre,decidim,logiciels,contrat,mission
---
On a beaucoup parlé ces dernières années de Decidim (« *Nous décidons* » en catalan), [une plateforme de démocratie participative](https://decidim.org/) mise en place par la municipalité de Barcelone depuis 2017. [Comme l'explique Yochai Benkler](https://www.barcelona.cat/metropolis/en/contents/imagined-community-practice-community), le projet Decidim constitue un remarquable exemple de [Partenariat Public-Commun](http://blogfr.p2pfoundation.net/2017/06/09/vers-partenariats-public-communs/) dans lequel un acteur public a choisi de développer une ressource dans un esprit de réciprocité afin que d'autres entités, qu'il s'agisse de collectivités ou d'organisations de la société civile, puissent s'en saisir, se l'approprier et participer à son développement :

> *Le système Decidim de Barcelone s'appuie sur une plateforme logicielle gratuite pour accroître la participation des citoyens dans la gouvernance de la ville et des projets municipaux. La plateforme Decidim constitue ainsi un modèle de partenariat Public-Commun, où la ville finance le développement d'une plateforme FOSS (Free and Open Source Software) qui est ensuite disponible pour toute autre ville ou entité du gouvernement. La plateforme a permis à des dizaines de milliers de citoyens de faire plus de 10 000 propositions de projets et de planification stratégique dans toute la ville, d'en débattre et de voter sur les propositions, y compris une forme de budget participatif.*

![](https://scinfolex.files.wordpress.com/2019/05/decidim.png?w=580&h=243&crop=1){.aligncenter .wp-image-12632 .size-gateway-home width="580" height="243"}

Alors qu'en France, la séquence du Grand Débat s'achève sur une [impression de cérémonial creux](http://www.slate.fr/story/175473/grand-debat-national-grande-deception) ayant surtout servi de diversion, sans réelle incidence sur les propositions finales du gouvernement, la plateforme Decidim a permis à Barcelone de co-construire avec les citoyens [un Programme en Commun, un Code d'éthique politique et un Plan de Choc.](https://wiki.remixthecommons.org/index.php?title=Barcelone_en_commun) Portée au pouvoir par le mouvement des Indignés, la liste [Barcelone En Commun](https://fr.wikipedia.org/wiki/Barcelone_en_commun) menée par la militante Ada Colau, avait certes de fortes connexions avec la société civile. Mais l'outil libre Decidim a joué un rôle non négligeable dans l'entretien de la dynamique participative. A l'inverse en France, les autorités utilisent majoritairement pour leurs consultations un outil propriétaire mis à disposition par la société Cap Collectif, faisant dire à certain-e-s que l'on assiste à un processus de [« privatisation de la démocratie »](https://blogs.mediapart.fr/quitterie-de-villepin/blog/300119/alerte-en-marche-vers-la-privatisation-de-la-democratie).

Mais il y a autre chose d'intéressant dans le projet Decidim et il faut plonger dans sa dimension juridique pour s'en rendre compte. Jusqu'à présent, j'avais retenu que le code source de Decidim était mis à disposition sous une variante de la licence GNU-GPL ([AGPL pour Affero General Public Licence](https://fr.wikipedia.org/wiki/GNU_Affero_General_Public_License)), c'est-à-dire une licence classique de logiciel libre permettant la réutilisation du programme à toutes fins à condition d'en partager à l'identique les modifications ([clause copyleft](https://www.gnu.org/licenses/copyleft.fr.html)). Néanmoins les choses sont un peu plus compliquées, car cette licence n'est pas le seul élément à prendre en compte pour savoir comment réutiliser le logiciel. Il faut en outre se reporter à [un Contrat social](https://medium.com/open-source-politics/le-contrat-social-de-decidim-un-texte-fondateur-7a8916213270) constituant un document séparé qui fixe des « garanties démocratiques » devant être respectées en cas d'usage de la plateforme.

Il existe déjà des projets Libres ou Open Source qui s'appuient sur un Contrat Social ([comme le projet Debian](https://www.debian.org/social_contract)) ou sur des principes communautaires de fonctionnement ([comme les Cinq Piliers de Wikipédia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Principes_fondateurs)). Mais Decidim se démarque par une articulation originale entre la licence libre sur le logiciel et ce Contrat social. J'y vois un apport substantiel ouvrant la voie à l'avènement de logiciels que l'on pourrait dire « à mission » (en référence à « [l'entreprise à mission »](https://fr.wikipedia.org/wiki/Entreprise_%C3%A0_mission) dont on parle beaucoup en ce moment).

C'est peut-être une piste à suivre pour dépasser certaines limites inhérentes à l'approche des logiciels libres, qui pèsent aujourd'hui lourdement sur leur cohérence d'ensemble.

### Un Contrat Social au-delà de la licence

Le site d'Open Source Politics, qui a [traduit le Contrat Social de Decidim en français](https://medium.com/open-source-politics/le-contrat-social-de-decidim-un-texte-fondateur-7a8916213270), en explique la philosophie générale en ces termes :

> *L'idée derrière la reprise de cette notion par les fondateurs de Decidim est d'assumer le développement d'un nouveau fonctionnement politique à travers l'adoption de cette plateforme. C'est donc la marque d'un renouvellement de la compréhension de notre participation, en tant qu'individus politiques, à la société. Cette conception renouvelée du poids politique du citoyen est issue directement, dans le cas de Decidim, de la relation étroite des leaders du projet avec le mouvement des Indignés, qui souhaitait explicitement refonder l'organisation du pouvoir politique pour obtenir une démocratie plus ouverte.*

Plus précisément, il s'agit d'une « *Charte valorisant les garanties démocratiques et la collaboration ouverte* » qui fixe une liste de principes que « *tous les membres du projet Decidim s'engagent sur l'honneur à respecter* » (je reviendrai plus loin sur ce point qui est important).

Voici un résumé de ces principes figurant dans la Charte :

-   **Logiciel libre et contenus ouverts :** le code de la plateforme doit rester sous licence AGPL. Tous les contenus de type « oeuvres » (photos, textes, vidéos, graphiques, etc.) doivent être diffusés sous CC-BY-SA et les données sous ODbL. Tous ces élément et les API figurant sur la plateforme doivent utiliser des standards ouverts garantissant l'interopérabilité.
-   **Transparence, traçabilité, intégrité** : Tous les contenus sur la plateforme doivent être accessibles et téléchargeables, L'origine de chaque proposition doit être connue, ainsi que la décision relative à son adoption, à son rejet ou son abandon. Les contenus doivent être affichés sans être manipulés et toute modification doit être documentée, transparente et contrôlable.
-   [**Égalité d'opportunité et indicateurs qualitatifs :** La plate-forme offre à tous les processus hébergés (propositions, débats, etc.) des chances égales de départ pour qu'ils puissent être vus, discutés, commentés, évalués ou traités sans discrimination d'aucune sorte.]{#65b4}
-   **Confidentialité des données :** La vie privée des participants et leur droit à la protection de leurs données personnelles doivent être respectés, de même que leurs droits démocratiques.
-   **Responsabilité et suivi :** Des engagements doivent être pris pour que les demandes des participants fassent l'objet de réponses et qu'une procédure d'évaluation soit mise en place à l'issue des consultations.
-   [**Amélioration permanente et collaboration inter-institutionnelle :** Les évaluations conduites doivent effectivement servir à améliorer continuellement la plateforme. Les différentes institutions et parties prenantes aux processus s'engagent à collaborer ensemble.]{#42e3}

![Utiliser Decidim, c\'est prendre un engagement un peu plus fort que celui de simplement respecter une licence libre. Image : Domaine Public. Source : Wikimedia Commons.](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Jacques-Louis_David%2C_Le_Serment_des_Horaces.jpg/1200px-Jacques-Louis_David%2C_Le_Serment_des_Horaces.jpg){width="526" height="405"}

### Une autre conception de la viralité

Le point le plus intéressant du Contrat Social de Decidim se situe néanmoins au niveau de la partie relative aux Conditions d'Utilisation de la plateforme (CGU) :

> ### *Conditions d'utilisation* {#d3f8 .graf .graf--h3 .graf-after--p}
>
> *Tous les points de cette charte doivent être reproduits dans le texte du contrat de licence que chaque organisation qui intègre Decidim à ses services établit avec les utilisateur.trice.s et ne doivent jamais être contredits.*

Ce point est confirmé et explicité [dans la FAQ du projet](https://decidim.org/faqs/) :

> Decidim est une plateforme de participation citoyenne faite avec les gens et pour les gens. \[...\] vous n'avez pas à payer pour télécharger le logiciel et l'utiliser. Vous pouvez l'utiliser comme vous le souhaitez dans votre organisation, du moment que vous respectez notre Contrat Social.

C'est là que l'approche de Decidim diffère de ce que l'on trouve habituellement dans l'univers du logiciel libre ou Open Source et je vais prendre quelques exemples pour le mettre en lumière.

Comme je l'ai déjà dit, la communauté Debian -- qui développe une distribution du système d'exploitation Linux -- a elle aussi [un contrat social](https://www.debian.org/social_contract.fr.html). Celui-ci fixe les principes et valeurs partagés par les développeurs formant la communauté, mais ces règles restent « internes » et ne se communiquent pas ensuite aux utilisateurs du logiciel, qui sont soumis simplement aux termes de la licence GNU-GPL. C'est la même chose pour [les Cinq Piliers de Wikipédia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Principes_fondateurs) : ces principes fixent la manière dont la communauté des contributeurs à l'encyclopédie collaborative se gouverne elle-même, mais ils ne s'imposent pas aux personnes qui souhaiteraient réutiliser uniquement le logiciel libre [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki/fr) avec lequel tourne Wikipédia ou les contenus sous Creative Commons de l'encyclopédie.

![RÃ©sultat de recherche d\'images pour ](https://image.slidesharecdn.com/debianjessie-150508050848-lva1-app6891/95/debian-jessie-12-638.jpg?cb=1431064108){width="452" height="339"}

Les choses sont différentes pour Decidim : la « communauté » du projet englobe ici à la fois les développeurs qui font évoluer le code, mais aussi toute personne ou institution réutilisant ce code pour mettre en place une plateforme basée sur ce programme. Le logiciel est sous AGPL, ce qui implique que toute modification soit reversée sous la même licence. C'est la vision classique de la « viralité » ou du « partage à l'identique », mais ici les choses vont plus loin, car le Contrat Social du projet se transmet lui aussi de manière virale via les CGU des plateformes s'appuyant sur ce code. L'usage du programme est donc irréversiblement lié au respect des valeurs et de la vision politique originale du projet Decidim.

Reprenons l'exemple de Wikipédia, si les Cinq Pilliers prenaient la forme d'un tel Contrat Social adjoint à MediaWiki, l'usage de ce logiciel impliquerait de respecter les principes fondateurs de Wikipédia, alors qu'il peut très bien aujourd'hui être utilisé pour mettre en place des projets à la philosophie différente, et voire même antagoniste, à celle de l'encyclopédie libre.

### Vers des logiciels libres « à mission » ?

Je trouve que la manière la plus efficace d'exprimer le changement que provoque l'approche de Decidim est de dire que cette combinaison originale de licence libre et de contrat social instaure ce que j'appellerai un « logiciel libre à mission ».

L'expression s'inspire du concept « [d'entreprise à mission](https://fr.wikipedia.org/wiki/Entreprise_%C3%A0_mission) » qui a fait l'objet de longues discussions ces derniers mois et a fini par connaître une traduction juridique dans la loi PACTE. Je n'entre pas ici dans les détails, car la manière dont le gouvernement a inscrit cette idée dans la loi [s'éloigne largement de l'intention initiale des promoteurs de cette notion](https://france.attac.org/nos-publications/les-possibles/numero-17-ete-2018/dossier/article/changer-l-entreprise-quand-la-montagne-accouche-d-une-souris)... Remontons simplement à la racine du concept d'entreprise « à mission » : il implique qu'une entreprise n'ait pas uniquement un but lucratif, mais inscrive en outre dans ses statuts une finalité sociale et/ou environnementale qu'elle devra respecter.

Ce changement entraîne que l'entreprise cesse d'être considérée simplement comme un « instrument » destiné à faire du profit. Elle retrouve de la sorte la forme d'une institution dévouée à la réalisation de ce que [le juriste Maurice Hauriou](https://www.persee.fr/doc/dreso_0769-3362_1995_num_30_1_1343) appelle une « idée d'oeuvre » à réaliser qui lui donne sa « raison d'être ». Ce principe téléologique justifie que l'institution se dote de moyens et d'organes pour la réaliser à travers ses membres qui doivent adhérer à cet objectif.

Decidim fait exactement la même chose avec son logiciel : celui-ci n'est plus seulement un instrument pouvant être utilisé pour réaliser n'importe quelle fin, mais une institution à part entière. L'articulation du contrat social et de la licence libre intègre une « idée d'oeuvre » à réaliser qui est indéfectiblement attachée au code source, et qui, via les CGU des plateformes, devient opposable à ceux qui la mettent en oeuvre, pour les forcer à respecter ces valeurs en cas où ils s'en écarteraient.

### Une conception non-libertarienne de la liberté

Cette vision de Decidim s'écarte assez sensiblement de la conception véhiculée par la tradition du logiciel libre. En effet, celle-ci a une conception assez « absolutiste » de la liberté qui s'exprime dans la manière dont sont définies les « Quatre libertés fondamentales du logiciel libre ». En particulier, la liberté 0 (ou « Liberté d'exécuter le programme comme vous le souhaitez ») est [ainsi présentée par la Free Software Foundation](https://www.gnu.org/philosophy/free-sw.fr.html) :

> *La liberté d'utiliser un programme est la liberté pour n'importe qui ou n'importe quelle organisation de l'utiliser sur n'importe quel système informatique, pour n'importe quelle tâche et sans être obligé de communiquer à ce sujet avec le développeur ou toute autre entité particulière. Dans cette liberté, ce qui compte est ce que veut faire l'utilisateur, pas le développeur ; en tant qu'utilisateur, vous êtes libre d'exécuter un programme comme bon vous semble et, si vous le redistribuez à quelqu'un d'autre, cette personne est libre de l'exécuter comme bon lui semble, mais vous n'êtes pas autorisé à lui imposer vos conditions.*

En réalité, le logiciel libre repose sur une [conception libertarienne de la liberté](https://fr.wikipedia.org/wiki/Libertarianisme), impliquant une suspension du jugement moral et un agnosticisme strict quant aux fins poursuivies. Les licences libres se contentent de garantir l'exercice des quatre libertés fondamentales de l'utilisateur : 1) exécutez le programme, 2) accéder au code source, 3) partager le programme, 4) pouvoir le modifier ; et la seule restriction qu'elles tolèrent consiste à fixer une obligation de partage à l'identique ([copyleft](https://fr.wikipedia.org/wiki/Copyleft)) pour garantir que ces libertés ne seront pas retirées une fois qu'elles ont été octroyées une première fois.

![RÃ©sultat de recherche d\'images pour ](https://webtv.centrale-marseille.fr/protected/videos/2012-02-23_16-43-29_699843/images/capture_1327487112_013467.jpg){width="438" height="328"}

Mais cela laisse entière la question de savoir à quoi le logiciel est utilisé : servira-t-il à faire marcher un drone de guerre ou un appareil médical destiné à sauver des vies ? Une licence libre s'interdit absolument de porter ce type de jugement et la FSF va même plus loin :

> *Un programme est un logiciel libre s'il donne toutes ces libertés aux utilisateurs de manière adéquate. Dans le cas contraire, il est non libre.*

Cela signifie que, de ce point de vue libriste « canonique », Decidim ne saurait être considéré comme un logiciel libre, étant donné que son Contrat Social implique que le programme ne peut être utilisé à n'importe quelle fin (y compris d'une manière qui serait absolument contraire à celles initialement portées par le projet).

On notera que d'un point de vue philosophique, la liberté peut être définie d'une autre manière que d'un point de vue libertarien. Chez Kant par exemple, il existe bien [une liaison nécessaire entre liberté et moralité](https://fr.wikipedia.org/wiki/Philosophie_pratique_de_Kant#La_libert%C3%A9), comprise comme des « *impératifs catégoriques* » que la raison se fixe. Ce qui le conduit à énoncer dans sa *Critique de la Raison Pure* :

> *Une volonté libre et une volonté soumise à des lois morales sont par conséquent une seule et même chose.*

On pourrait donc dire que Decidim met en oeuvre une vision « kantienne » de la liberté qui se manifeste par des valeurs et par une idée d'oeuvre répercutée viralement par le biais son Contrat Social. Ainsi les promoteurs du projet Decidim ont-ils la garantie que le logiciel qu'ils ont créé servira la « vision du Monde » qu'ils se sont donnés pour mission de faire advenir (contribuer à une refondation de la démocratie).

### Dépasser certaines contradictions du logiciel libre

Il a existé dans le monde du logiciel un précédent intéressant ayant déjà soulevé des questions approchantes. Il s'agit de celui de [la licence JSON](https://www.json.org/license.html) (attachée au [format de données textuelles JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation) dont l'usage est aujourd'hui très répandu). Le créateur du JSON -- [Douglas Crockford](https://fr.wikipedia.org/wiki/Douglas_Crockford) -- avait créé en 2002 pour diffuser ce format une licence spécifique qui ressemblait en tout point à une licence Open Source, à ceci près qu'elle contenait cette clause incongrue :

> *The Software Shall Be Used for Good, and Not For Evil / Le logiciel doit être utilisé pour faire le bien et non le mal.*

Ce rajout -- qui dans l'esprit de Crockford se voulait un pied-de-nez trollesque à la fameuse phrase de George Bush sur « l'axe du mal » -- a néanmoins posé quelques problèmes. Car le format JSON étant de plus en plus largement utilisé, cette référence au Bien et au Mal a fini par mettre mal à l'aise certaines entreprises qui l'utilisaient. A tel point que la firme IBM a demandé officiellement à Douglas Crockford de pouvoir utiliser le JSON pour « faire le mal » (ce qui lui fut accordé...).

![](https://scinfolex.files.wordpress.com/2019/05/bien.png?w=390&h=277){.wp-image-12647 width="390" height="277"}

On comprend que les juristes de l'entreprise aient voulu dissiper le risque qui s'attachait à des termes aussi flous que « Bien » ou « Mal », mais que ce soit IBM qui ait demandé à pouvoir s'en affranchir est assez croustillant. Car [cette firme s'est distinguée](https://www.zdnet.fr/actualites/la-plainte-contre-ibm-pour-collaboration-au-nazisme-a-ete-retiree-2062702.htm) en vendant dans les années 30 aux nazis des machines à cartes perforées qui servirent à l'organisation de la Solution Finale et aujourd'hui encore, son activité reste au centre de polémiques, notamment du fait de son implication dans les solutions de reconnaissance faciale [avec recours à des méthodes assez contestables](https://www.linformaticien.com/actualites/id/51597/quand-la-reconnaissance-faciale-fait-fi-du-consentement.aspx).

Mais IBM est aussi (et ce n'est pas le moindre des paradoxes) l'entreprise que l'on cite toujours comme représentant le « Champion du Libre et de l'Open Source ». Elle compte en effet parmi [les contributeurs les plus importants au logiciel Linux](https://www.developpez.com/actu/188849/Quelles-sont-les-entreprises-qui-contribuent-le-plus-aux-projets-open-source-Microsoft-positionne-en-tete-sur-GitHub/) et est réputée avoir été l'une des premières grandes firmes capitalistes à avoir refondé sa stratégie sur le logiciel libre. Cela l'a conduit l'année dernière au rachat de la société RedHat, spécialisée dans l'édition de distributions GNU/Linux, [pour la spectaculaire somme de 34 milliards de dollars](https://www.usine-digitale.fr/article/ibm-rachete-red-hat-pour-34-milliards-de-dollars-afin-de-se-renforcer-dans-le-cloud-hybride.N761774).

La situation d'IBM n'est cependant plus isolée et ce sont aujourd'hui les principales entreprises du numérique, y compris même les GAFAM, qui utilisent et soutiennent les logiciels libres et Open Source. Avec à la clé, l'immense paradoxe que les entreprises les plus impliquées dans les dérives du [capitalisme de surveillance](https://www.monde-diplomatique.fr/2019/01/ZUBOFF/59443) sont aussi devenues des soutiens incontournables du logiciel libre et l'incorporent dans leurs produits en poursuivant des fins plus que discutables...

Posons donc la question qui dérange : et si Linux, par exemple, avait été dès le début -- comme Decidim -- un « logiciel libre à mission », appuyé sur un contrat social portant un certain nombre de valeurs, comme la protection inconditionnelle de la vie privée ? Est-ce que la face du Monde n'en aurait pas été changée et est-ce qu'on aurait pas évité de sombrer dans ce genre de contradictions ?

### Une piste à expérimenter ?

L'exemple de Decidim est donc très inspirant et je trouve particulièrement remarquable l'élégante simplicité avec laquelle le contrat social s'articule à la licence libre. A vrai dire, des tentatives ont déjà eu lieu ces dernières années pour essayer de « téléologiser » des licences libres, notamment dans le sillage des réflexions [sur les licences à réciprocité](https://scinfolex.com/2014/09/22/comprendre-le-principe-des-licences-a-reciprocite-en-5-minutes/), dont j'ai parlé à de nombreuses reprises sur ce blog.

Maïa Dereva avait notamment proposé [une licence Contributive Commons](http://contributivecommons.org/la-licence-contributive-commons/), qui comptait plusieurs éléments, parmi lesquels [un « Code Social »](http://contributivecommons.org/modeliser-code-social/) exprimant, entre autres choses, un faisceau de valeurs. La démarche était intéressante, mais elle aboutissait à un résultat à mon sens trop complexe pour être opérationnel, là où la solution employée par Decidim me paraît avoir le mérite de la simplicité, ce qui est important pour fluidifier les usages.

![](https://i0.wp.com/contributivecommons.org/wp-content/uploads/sites/5/2016/04/contributive-commons-outils-300x194.png){width="330" height="213"}

L'histoire n'est donc pas terminée et il sera intéressant de voir si d'autres initiatives arrivent à s'emparer de cette nouvelle brique et, pourquoi pas, partagent entre elles un même Contrat Social, servant de socle commun à une coalition d'acteurs rassemblés autour des mêmes objectifs de transformation sociale.
