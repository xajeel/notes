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

---

## Template Literals

```
let name1 = 'sajeel';
let name2 = 'ali';
```

Want to merge these values to make one String
```
console.log(name1 + ' ' + name2);
```

But using literal we can do this 
```
console.log(`${name1} ${name2}`);
```

## Ternary Operator

Lets say we have an situation where we want to return recipe1 when a certain flag is true & recipe2 when flag is false

condition ? statement1 : statement2
```
let showRecipe = true;

function getRecipeOne(name){
  return name;
}

function getRecipeTwo(name){
  return name;
}

showRecipe ? console.log(getRecipeOne('pizza')) : 
console.log(getRecipeTwo('Coke'))
```

---