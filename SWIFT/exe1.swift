func fibonacci(n:Int) -> Int{
    if n==0 || n==1 { return 1}
    let f = fibonacci(n : n-1) + fibonacci(n: n-2)
    return f
}
let f = fibonacci(n: 6)
print(f)