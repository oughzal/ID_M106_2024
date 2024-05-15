struct Book{
    var title : String
    var isbn : Int
    var auteur : String
    var disponible : Bool
}

struct Biblio{
    var list : [Int:Book] = [:]

    mutating func addBook(book : Book){
        list[book.isbn] = book
    }
    mutating func deleteBook(isbn : Int){
        if list.keys.contains(isbn){
            list[isbn] = nil
        }
    }
    mutating func updateBook (book : Book){
        list[book.isbn] = book
    }
    func searchByTitle(title : String) -> [Book] {
        return list.values.filter{ book in book.title.contains(title)}
    }
    func searchByAuthor(author : String) -> [Book]{
        return list.values.filter{ book in book.auteur.contains(author)}
    }
    func searchByIsbn(isbn : Int) -> Book? {
        return list.keys.contains(isbn)? list[isbn] : nil
    }
}