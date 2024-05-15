fun main(args: Array<String>) {
    var list = ListOf(1,2,3,4)
    var list2 = list.map{e :Int -> e*2 }
    list.forEach{e :Int -> print(e.toString())}

}