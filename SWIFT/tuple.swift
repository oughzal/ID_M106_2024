var coordinates : (Int,Int) = (10,19);
let (x,y) = coordinates
coordinates.0 = 40
print(coordinates.0);

var point : (x : Int , y : Int) = (20,20);
point.x = 30;
print(point.x);

var i : Int = 1
while i <= 10 {
    print(i)
    i += 1
}
i=1
repeat {
    if i == 4 {continue}
    print(i)
    i += 1 
} while i <= 10


