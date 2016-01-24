2016.01.24 by genus
This (ReadMe.txt) file explains templates Folder Structure of this application(gdg_flask)

Every folder has prefix 'gdg-'.

[gdg-base]
The Files in the 'gdg-base'[folder] is always called when application is requested.
Every requests will call files in the 'article'[folder] and that files(in the article folder) will call files in the 'gdg-base'[folder]

If you want to rend any templates, you just call files in the 'gdg-article'.
