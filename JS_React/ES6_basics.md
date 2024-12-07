# ES06 Basics ( Javascript )

## && and || ( AND  & OR ) Operators

' && ' and operator checks if the first value is true then its check the second value  but if the first value is not true then it will not look at the second value.
' || ' OR operator checks the second value even if the first value is false

```
function myName(name){
  return name;
}

let a = true;
let b = true;

console.log(a && myName('sajeel'));

//  Ouput: sajeel

```
```
function myName(name){
  return name;
}

let a = false;
let b = true;

console.log(a && myName('sajeel'));

// Ouput: False

```