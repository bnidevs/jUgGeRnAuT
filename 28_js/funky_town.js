var fibonacci = (n) => {
  if(n < 2){
    return n;
  }else{
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

var gcd = (a, b) => {
  if(b == a){
    return a;
  }else if(a == 0){
    return b;
  }else if(b == 0){
    return a;
  }else{
    if(b > a){
      b = b % a;
      return gcd(a, b);
    }else{
      a = a % b;
      return gcd(a, b);
    }
  }
}

var randomStudent = () => {
  var names = ["brian", "amy", "catherine"];
  return names[Math.floor(Math.random() * 3)];
}
