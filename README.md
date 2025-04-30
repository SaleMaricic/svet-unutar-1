Ovaj Python program vizualizuje hijerarhijsku strukturu sfera u 3D prostoru, koje su raspoređene kao da su "svetovi unutar sveta", počevši od jedne centralne sfere.

Funkcija generate_world_inside_one_3d(depth=4, shrink_factor=0.5)
Ova rekurzivna funkcija generiše strukturu sfera u 3D prostoru.

Ulazni parametri:

depth: dubina rekurzije, tj. koliko "nivoa svetova unutar svetova" se pravi.

shrink_factor: za koliko se smanjuje radijus sfera na svakom nižem nivou.

Algoritam:

Počinje od centra (0,0,0).

Na svakom nivou dodaje 6 sfera raspoređenih oko roditeljske.

Čuva sve tačke u listi points i linije koje povezuju roditelj-decu u lines.

Na kraju se prikazuje 3D interaktivni prikaz strukture, nalik fraktalnom drvetu ili molekulskoj mreži, gde se vidi kako se svet "granato" razvija u prostoru.

boje sfera odražavale njihovu udaljenost od centra (ili nivo u hijerarhiji)
