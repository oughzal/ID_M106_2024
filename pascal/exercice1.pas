program bonjours;
var
    A : real;
    B : String;
begin
    write('saisir votre nom : ');
    read(B);
    write('Entrez votre âge : ');
    read(A);
    write('Bonjour Mlle',B);
    write('tu a ',A,' ans');
    A := A * 10;
    write('Bravo ', A , 'fois')
end.
// Exercice
// saisir votre nom : Khadija
// Entrez votre âge : 17
// Bonjour Mlle Khadija
// tu a 17 ans
// Bravo 170 fois