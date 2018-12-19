var fibonacci = () => {
  var n = document.getElementById('fibnum').value;
  var window = [0, 1];

  if(n < 2){
    document.getElementById('fibval').innerHTML = (window[n]);
  }else{
    var inc = 2;
    while(inc <= n){
      window[inc % 2] = window[(inc + 1) % 2] + window[inc % 2];
      inc++;
    }
    document.getElementById('fibval').innerHTML = (window[(inc - 1) % 2]);
  }
}

var gcd = () => {
  var a = document.getElementById('gcdA').value;
  var b = document.getElementById('gcdB').value;
  document.getElementById('gcdval').innerHTML = gcdhelper(a, b);
}

var gcdhelper = (a, b) => {
  if(b == a){
    return a;
  }else if(a == 0){
    return b;
  }else if(b == 0){
    return a;
  }else{
    if(b > a){
      b = b % a;
      return gcdhelper(a, b);
    }else{
      a = a % b;
      return gcdhelper(a, b);
    }
  }
}

var randomStudent = () => {
  var names = ["brian", "amy", "catherine"];
  document.getElementById('rsval').innerHTML = names[Math.floor(Math.random() * 3)];
}
