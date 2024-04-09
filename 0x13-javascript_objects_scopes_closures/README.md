# 0x13. JavaScript - Objects, Scopes and Closures

## An object is a collection of related data.
```
example:
	const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf: function () {
    console.log(`Hi! I'm ${this.name[0]}.`);
  },
};
```
## Closure is a combination of a function bundled together with references to its sorrounding state. 
* closure give access to an outer function's scope from an inner function
