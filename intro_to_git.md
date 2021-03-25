# Introduction à git

#### Sommaire
- Pourquoi on utilise git
- Travail seul sur un projet git
- Forker un projet git
- Collaborer sur un projet git
- Git et Github pour le devops

## Pourquoi on utilise git

- Pouvoir avoir différentes versions de son travail
- Ne pas avoir peur de casser toute sa codebase avec une feature
- Pour travailler a plusieurs sans se gener grace aux branches
- Git a un ecosystème très developper, tout les developpeurs l'utilise
- Beaucoup d'automatisation sont possible grace a git

----

## Travail seul sur un projet git
### Creer un projet
On vas sur github et on creer un nouveau repository<br>
On clone le repository sur notre machine `git clone`<br>
On y met notre code `mv files/path destination/path`<br>
On peut faire notre premiere sauvegarde<br>
`git add *`<br>
`git commit -m "my first commit"`<br>
`git push origin master`<br>

### Le workflow sur un projet
- `git add`
- `git commit -m`
- `git push origin master`

### Si on fait des changement sur une autre machine
- `git pull origin master`

---

## Forker un repository git
Ce que l'on a fait hier.

### Commandes utiles

- `git remote -v` pour voir les repository distants lier a votre repository (d'autres sauvegardes en cloud)
- `git pull upstream master` pour mettre a jour votre repository avec la derniere version officiel

---

## Collaborer sur git

Vous pouver inviter vos collaborateur sur github.

### Travailler avec des branches

La branche **master** c'est toujours la branche avec la version final du projet qui sera mis en production
- `git checkout -b new_branch_name` pour creer et aller sur la branch
- `git push origin new_branch_name` pour sauver la branch sur github
- `git pull origin new_branch_name` pour aller chercher la dernière version de votre branch

**Merger** sa branche dans master avec une **pull request**
- aller sur github dans l'onglet `pull request` et faite `new pull request`

Resoudre les conflicts
- `git checkout new_branch_name`
- `git pull origin master`
- `git status`
- resoudre les conflicts
- `git add`
- `git commit`
- `git push`
- merger la branch sur github

---

## Git et Github pour le devops
Pendant la semaine on vas apprendre executer des actions automatique grace aux changement d'etat de git.
On vas apprendre a tester le code automatiquement.
Et si les test sont bon alors on met la derniere version du code en production automatiquement.