/*
  your PPTASK:
  
  First, familiarize yourself with the given html file for this work.

      then...

  Test drive each bit of code in this file,
  and insert comments galore, indicating anything
  you discover,
  have questions about,
  or otherwise deem notable.

  Have the given html file open as you work.
  
  Write with your future self or teammates in mind.
  
  If you find yourself falling out of flow mode, consult 
  - other teams
  - MDN

  A few comments have been pre-filled for you...
  
  (delete this block comment once you are done)
*/





// Team Phantom Tollbooth :: Clyde Sinclair, Fierce Dragon 
// SoftDev pd0
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");
//goes straight into console 
var i = "hello";
var j = 20;
//typing this variables out returns their respective values
//assign an anonymous fxn to a var
var f = function(x) 
{
    var j=30;
    return j+x;
};
//works in console

//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
              return x+30;
          }
        };

//access the fields by saying object.field !

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist");
    var newitem = document.createElement("li");
    newitem.innerHTML = text;
    list.appendChild(newitem);
};
//change is visible immediately (no reload required)

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li');
    listitems[n].remove();
};

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red');
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue');
	}
    }
};


//insert your implementations here for...
let fib = function(n){
    if(n < 2){
        return n;
    }
    return fib(n - 1) + fib(n - 2)
}
let fact = function(n){
    if(n == 0){
        return 1;
    } 
    return n * fact(n - 1)
}
let gcd = function(a, b){
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}


// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.
const myFxn = (param1, param2) => {
    retVal = param1 + param2;
    return retVal;
};

