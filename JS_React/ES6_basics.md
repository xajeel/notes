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

## Objects ( Dictionary )

```
const id = 1;
const productName = 'Apple';
const ratting = 5;

const product = {
  id:id,
  productName: productName,
  ratting: ratting,
};

console.log(product);

// Ouput: { id: 1, productName: 'Apple', ratting: 5 }
```

Short hand property: When the key & value names are same then we can only write keys names

```
const product2 ={
  id,
  productName,
  ratting,
};

console.log(product2);

// Ouput: { id: 1, productName: 'Apple', ratting: 5 }
```

To get something ( value ) from the dictionary we can use 

```
console.log(product.productName);
```

We can do the same thing by Deconstructing the Object and giving and alias ( Here `x` is alias)

```
const {ratting: x} = product2;
console.log(x)
```

In case of array 

```
let array = [1,2,3]

const [fisrt, second, third] = array
console.log(fisrt, second, third)
```

If we give a fourth value in the [ ] we will get `undefined` as our array has only 3 elements.

---

## Functions 

```
function mulNumber(num1, num2){
  return num1*num2;
}

console.log(mulNumber(3, 5))
```

function with default parameters 

```
function mulNumber2(num1=2, num2=4){
  return num1*num1
}

console.log(mulNumber2())
```

spread

```
const array1 = [1,2,3]
const array2 = [11,12,13]

console.log(array1)                     // Ouput: [ 1, 2, 3 ]
console.log(... array1)                 // Output: 1 2 3
console.log(...array1, ...array2)       // Output: 1 2 3 11 12 13
console.log([...array1, ...array2])     // Output: [ 1, 2, 3, 11, 12, 13 ]
console.log(0,99, ...array1, ...array2) // Output: 0 99 1 2 3 11 12 13
```

Rest Parameters 
We can give the spread a function parameter as well but it will b the last parameter in parameter 

```
function getInfo(a, b, ...c){
  console.log(a, b, c);
  return '';
}
console.log(getInfo(1,2,3,4,5,6,7))

// Output: 1 2 [ 3, 4, 5, 6, 7 ]
```
This will give the value of first two parameters and spread ( retuen in a list ) the remaining parameters values