#sqlgo

# Qu'est-ce que le projet sqlgo ?
sqlgo est un outil conçu pour les tests d'injection SQL à des fins éducatives, et non illégal. Rappelez-vous : POUR UN USAGE ÉTHIQUE UNIQUEMENT !!!

# comment installer sqlgo ?
```
git clone --profondeur 1 https://github.com/HeisenbergCipherCracker/sqlgo.git
```
copiez la commande ci-dessus sur le terminal et accédez au répertoire sqlgo
assurez-vous que git est installé sur votre système.

# dépendances
- utilisez les commandes suivantes pour installer les dépendances sqlgo en utilisant pip
```
pip install -r requirements.txt
```
```
pip3 install -r requirements.txt
```
**pour le système d'exploitation Windows**
```
python -m pip install -r requirements.txt
```
python3 -m pip install-r requirements.txt
**pour les systèmes basés sur Unix**



**Afficher le menu d'aide**
```
python3 sqlgo.py --help
```

**Mettre à jour le programme**

```
python3 sqlgo.py --update
```

**Lancer une attaque**
```
python3 sqlgo.py -u http://www.target-url?id=1 --port <numéro de port> --level <niveau> --verbose <verbose> --tamper <tamper> --dbms<SGBD> --décharge
```
# Fonctionnalités de sqlgo
1) Prend en charge les attaques par injection SQL contre MySQL
2) Prise en charge de l'envoi des différentes charges utiles, y compris la requête de pile, le délai et l'union de toutes les charges utiles et autres charges utiles fortes.
3) fournit de nombreux scripts de falsification pour falsifier les charges utiles afin de contourner le WAF ou les systèmes de détection d'intrusion (IDS).
4) Fournit diverses techniques d'encodage pour encoder
5) Détection et scanner automatiques des vulnérabilités d'injection SQL


# Comment signaler les bugs ?
les bugs seront acceptés s'ils existent et vous pouvez les signaler depuis la page github de sqlgo. vous pouvez accéder à l'onglet Problèmes dans le github et signaler le bogue dans la phrase claire.