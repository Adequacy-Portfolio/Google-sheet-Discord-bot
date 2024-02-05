Instructions d'installation

Pour exécuter ce projet, vous devez avoir Python version 3.11.0 installé sur votre système.

Installation de Python 3.11.0

Vous pouvez télécharger Python 3.11.0 depuis le site officiel de Python : https://www.python.org/downloads/release/python-3110/. Suivez les instructions d'installation pour votre système d'exploitation.

Dépendances

Après avoir installé Python 3.11.0, vous devez installer les dépendances suivantes à l'aide de pip :

discordpy
jsons
os.path
json
google-auth
google-auth-oauthlib
google-api-python-client

Pour installer ces dépendances, exécutez la commande suivante dans votre terminal ou votre invite de commandes :

pip install discordpy jsons google-auth google-auth-oauthlib google-api-python-client

Instructions de configuration du bot

Avant d'exécuter le bot, assurez-vous de suivre ces instructions de configuration :

1. Fichier de configuration :
   - Remplissez le fichier configuration.json avec les informations requises :
       - Jeton pour le bot
       - Nom et identifiant de la feuille Google où vous souhaitez stocker les informations
   - Identifiant secret du bot : Correspond à l'identifiant du webhook
   - Le champ "channel" correspond au canal où vous avez configuré le webhook pour envoyer des messages via les paramètres du serveur Discord.

2. Code de Google App Script :
   - Copiez le code Google Apps Script dans l'extension Google Apps Script dans Google Sheets.
   - Modifiez l'URL du webhook dans le code Google Apps Script par votre URL de webhook.

3. Identifiants de l'API Google :
   - Placez le fichier de clés obtenu à partir de l'API Google Sheets à l'intérieur du dossier google_api.

4. Notes supplémentaires :
   - Confirmez que vous avez ajouté un déclencheur "à l'édition" dans Google Sheets.
   - Lors du premier lancement du bot et lors de l'utilisation d'une commande slash, vous serez invité à vous connecter à votre compte Google.
   - Notez que les noms de colonnes visibles dans les captures d'écran doivent être saisis manuellement. Cependant, le bot n'a pas besoin d'eux pour remplir les données car il les saisira quand même.
