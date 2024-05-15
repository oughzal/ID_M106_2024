// Une extension permet d'ajouter de nouvelles fonctionnalités à un type existant,
// ce qui inclut le rajout de méthodes, de propriétés calculées, et plus encore.
extension String {
    // Ajout d'une méthode à la structure de base 'String' de Swift.
    func inverser() -> String {return String(self.reversed())}
}
let exemple = "Bonjour"
print("Bonjour".inverser()) // Affiche "ruojnoB"
