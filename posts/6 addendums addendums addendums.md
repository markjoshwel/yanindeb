# addendums addendums addendums

Turns out, I didn’t get everything I’ve noted down in Week 5’s post correct.  
(what a surprise)

So here they are, as addendums to the previous post.

- object declaration syntax

  ```js
  const obj = {
    key: value,
    // ...
  };
  ```

- iteration syntax (for x in y loop, but for arrays)

  ```js
  for (declaration of iterable) {
    // ...
  }
  ```

- functions returning themselves as objects

  ```js
  function Greeting(name) {
    this.name = name;
    this.greet = function() {
      console.log(`Hello, ${this.name}!`);
    };
  }
  ```

- reminder that `\n` will only work if printing to console (i think), else use `<br>`

…since the basics were learn’t last week anyways, this week yields a relatively short post compared to the last.

au revoir!

![dog head on penguin image](https://files.catbox.moe/konjj4.jpg)
