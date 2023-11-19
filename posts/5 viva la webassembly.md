# viva la webassembly

First and foremost, as per the CA, proof-of-completion screenshots:

Before anything, father, I have a confession to make, I am just watching the course on 2x and just skimming through it.

Fret not, I (think I) have enough experience with other programming languages like Python, Zig and Rust to help me fill in the stop gaps. Even if I didn't know any other lang other than Python I think I would still be fine.

Also, I hate JavaScript. To think our infrastructure is built on this. Thankfully TypeScript exists,
but I don't think it's good enough of a solution. Viva la WebAssembly.

---

Anyways, in JavaScript:

- Everything is an object (for better or for worse)

- Multiple variable assignment is cool

- The idea of a `Number` type is weird

- Mutability is nice  
  (python only has type annotations, and ~technically~ everything is mutable, while virtually most other langs have some form of mutability)

- Objects are basically JSON but first-class (i wonder what JSON stands for?)
  
  Indexing them and accessing via a property both works which is neat if not standard in scripting languages

- CamelCaseCamelCaseCamelCase

- Arrays are objects that are basically Python lists  
  ...and deleting will create an empty item

- Multiline strings with `\` is weird but ok  
  Python and especially Zig win on how to do multiline strings

- Comments are like comments in languages where it doesn't start with a `#` or after an `;`  
  ...so `/* block comments */` exist (and i like em)

  also seeing comments included in objects in the REPL is actually cool, why python don't do same :(

- I have always and still hated RegEx-es, cool to see as a first-class feature of the language but feels gimmicky  
  (but it does make complete sense for a web-first language)

- `==` and `===` is different because ☆*:.｡.o(≧▽≦)o.｡.:*☆

- Postfix single-increment and single-decrement operators exist (`++` and `--`)

- Operators!  
  `&&` is and  
  `||` is or  
  `! ` is not  

  (everything else is as you expect coming from python, except for some python bitwise operators)

  **note:** js bitwise operands operate on 32 bits even though numbers are 64 bit floats/`f64`  
  (how fun!)

- Truthy and falsy values exist!  
  (aiyo)

- Instantiate objects with `new object`, e.g., `new Map();`

- Type check with `typeof expression`  
  (analogous to `type()` in python or `@typeOf` in zig)

- NaN (not a number) exists as a first-class thing and is weird  
  check with `Number.isNan()`

- You can check for properties using `.hasOwnProperty()`  
  kinda cool i wonder how many other langs have something like this even if only determinable at compile time

- Sets are the same as Python sets

- Maps are (massive oversimplication!) objects that store key-value pairs but:

  - Object keys are strings or symbols  
    Map keys can be any data type

  - Maps maintain insertion order

  - Maps have functions for key access and manipulation - `set()`, `get()`, `delete()`, `has()`, etc

  - Maps have a `.size` property

  - Maps can be enumerated, yielding a `[key, value]` array  
    Enumerating through objects only return keys

  basically use them when order is important, analogous to `OrderedDict` in Python

- Functions are objects and can be passed to other functions ([first-class functions](https://en.wikipedia.org/wiki/First-class_function))  
  
  (so what is a monad?)

- Objects passed into functions are passed by references  
  
  ...so either create a new object to return or [shallow](https://developer.mozilla.org/en-US/docs/Glossary/Shallow_copy) or [deep copy](https://developer.mozilla.org/en-US/docs/Glossary/Deep_copy) the object

- Functions do not have named arguments but can be given default _positional_ values

- Functions are given an `arguments` array, similar to `argv` for `main()` functions but without needing to declare it as a argument

  Analogous to `def function(*arguments):` in Python

  However, you can write `*arguments` as `...arguments` in JavaScript as the last argument

---

Syntaxes:

- initialisation syntax

  ```js
  var   name;
  let   name;
  const name;
  ```

  but why?  
  **note:** results in undefined if given a value before being used

- declaration syntax

  ```js
  var   name = expression ;  // function-scope; mutable (global if not in a func)
  let   name = expression ;  // block-scope   ; mutable
  const name = expression ;  // block-scope   ; immutable (cannot change aft decl)
  ```

- conditionals syntax

  ```js
  if (expression) {
    // ...
  } else if {
    // ...
  } else {
    // ...
  }
  ```

- conditional if one-liner

  ```js
  if (condition) expressionTrue ;
  ```

- conditional ternary expression syntax (one-line if)

  ```js
  condition  ?  expressionTrue : expressionFalse ;
  ```

- switch syntax

  ```js
  switch (expression) {
    case value:
      // ...
    default:
      // ...
  }
  ```

  **note:** break out of every case like C++

- iteration syntax (for loop)

  ```js
  for ( init ; condition ; statement ) {
    // ...
  }
  ```

- enumerative iteration syntax (for x in y loop)

  ```js
  for (declaration in iterable) {
    // ...
  }
  ```

  **note:** `declaration` here could be `var i` etc

- conditional iteration syntax - check first; do later (while loop)

  ```js
  while (condition) {
    // ...
  }
  ```

- conditional interation syntax - do first; check after (while loop)

  ```js
  do {
    // ...
  } while (condition) ;
  ```

  **note**: remember the trailing semicolon

- function declaration syntax

  ```js
  function name([argument, ...]) {
    // ...
  }
  ```

- function declaration syntax using function expressions

  ```js
  function([argument, ...]) {
    // ...
  }
  ```

  **note:** can be assigned to a variable or be used anonymously

- function declaration syntax using an arrow function

  ```js
  ([argument, ...]) => {
    // ...
  }
  ```

  **note:** can be assigned to a variable or be used anonymously

---

...i am not touching promises, async and await just yet

and yes i know i've used `arguments` interchangeably with `parameters`, sue me

good chance i have oversimplified the language and i might look back at this years into the future and just tense up in shame

...but can you tell i don't like js? (you're telling me i need a guard clause to check if an argument is an object? in an oop language?)  

why must've java shape js instead of the functional language it could've been :^)

viva la webassembly and the eventual, already progressing liberation of the web!

---

okay ciao

![a cute panel from yotsubato]()
