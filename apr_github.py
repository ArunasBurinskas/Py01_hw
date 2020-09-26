# pirmas žingsnis - sukuriame tuščią gir direktoriją:
git init

# antras žingsnis - paimame visus repozitorijoje esančius failus:
git add .

# galima pasižiūrėti kas yra:
git status

# pirmam kartui dar reikia sukonfiguruoti:
git commit
git config --global user.email "burinskas.arunas@gmail.com"
git config --global user.name "arunas"


# jeigu spaudžiu vėl
git commit
# tai išėjimui gali prireikti:

:qa
# ir enter. Tai aiškino mums 2020-07-11 dieną

# trečias žingsnis - parašau žinutę, kurioje nurodau kas pasikeitė mano siunčiamuose naujai į GitHubą failuose
git commit -m "mano pirmas commitas"

# pasitikrinu:
git status

# ketvirtas žingsnis - susieju savo kompo repozitoriją su GitHubo repozitorija (reikia įvesti savo gmailą ir paswordą)
git remote add origin https://github.com/ArunasBurinskas/Py01_hw.git

# jei susiejimas jau yra (prisiloginęs), kartoti nereikia

# penktas žingsnis - stumiu į GitHubą
git push -u origin master

# pastaba: kad ne visus failus keltu, reikia išmokti naudoti komandą ignore

________________________________

# Kai ką nors pakeiti repozitorijos failuose, Pycharmo terminale parašius:
git status
# raudonai parašo tuos failus, kuriuose pakeitimai buvo atlikti.
# Todėl vėl supušinus su nauja žinute, GitHube, atsiras ir tie pakeitimai

_______________________________
# jei GitHube su pieštuku kažką pakeičiu, galima failus su pakeitimais pulinti atgal:
git pull

_______________________________
# 2020-07-12 Rolandas aiškino apie:
