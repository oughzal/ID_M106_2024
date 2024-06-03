#ps1 : extension des fichier powershell ps(postscript)

# Afficher la date du jour sous format dd/mm/yyyy (27/05/2024)
Get-Date -Format dd/yy:yy
#Afficher le dossier current du travail
Get-Location # équivalent a pwd(linux)
#supprimer le dossier c:\doc\REP1 et son contenu
Remove-Item c:\doc\REp1 -Recurse
#vérifier si le fichier c:\doc\file.txt existe
test-path c:\doc\file.txt
#Ecrire "Hello world" dans le fichier c:\doc\file.txt
Set-Content -Path c:\doc\file.txt -Value "Hello world"
# créer un utilisateur avec le nom d'utilisateur et mot de passe saisie au clavier
$nomUtilisateur = Read-Host "Entrez le nom de l'utilisateur"
$password = Read-Host "Entrez le mot de passe" -AsSecureString
New-LocalUser -Name $nomUtilisateur -Password $password
