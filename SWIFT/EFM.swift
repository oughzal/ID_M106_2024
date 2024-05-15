//Q13
struct Événement {
    var id: Int
    var titre: String
    var artiste: String
    var nombreDePlaces: Int

    init(id: Int, titre: String, artiste: String, nombreDePlaces: Int) {
        self.id = id
        self.titre = titre
        self.artiste = artiste
        self.nombreDePlaces = nombreDePlaces
    }
}
//Q14
struct Client {
    var id: Int
    var nom: String
    var réservations: [Int] // Liste des IDs des événements réservés

    init(id: Int, nom: String, réservations: [Int] = []) {
        self.id = id
        self.nom = nom
        self.réservations = réservations
    }
}
//Q15
class GestionnaireRéservations {
    var événements: [Int: Événement] = [:]
    var clients: [Int: Client] = [:]

    func ajouterÉvénement(événement: Événement) {
        événements[événement.id] = événement
    }

    func ajouterClient(client: Client) {
        clients[client.id] = client
    }

    func réserverÉvénement(idÉvénement: Int, idClient: Int) {
        guard let événement = événements[idÉvénement],
              événement.nombreDePlaces > 0,
              let client = clients[idClient] else {
            return
        }
        événements[idÉvénement]?.nombreDePlaces -= 1
        clients[idClient]?.réservations.append(idÉvénement)
    }

    func annulerRéservation(idÉvénement: Int, idClient: Int) {
        guard let index = clients[idClient]?.réservations.firstIndex(of: idÉvénement) else { return }
        événements[idÉvénement]?.nombreDePlaces += 1
        clients[idClient]?.réservations.remove(at: index)
    }

    func afficherÉvénements() {
        for événement in événements.values {
            print("\(événement.titre) par \(événement.artiste), Places restantes: \(événement.nombreDePlaces)")
        }
    }

    func afficherClients() {
        for client in clients.values {
            let réservés = client.réservations.map { "\(événements[$0]?.titre ?? "Inconnu")" }.joined(separator: ", ")
            print("\(client.nom) a réservé: \(réservés)")
        }
    }
}