# lottie lottie lottie

![lotte from parallel world pharmacy/isekai yakkyoku](https://files.catbox.moe/3i518z.png)

I had my doubts, but Lottie animations are cool.

I almost used a second library for interactivity, but I just read the docs, and turns out to always start an animation when a button is clicked,
you can just `seek()` the player to the beginning, or 0.

```js
const lottie = document.querySelector("dotlottie-player");

const button = document.querySelector("button");
button.addEventListener("click", () => {
  lottie.seek(0);
  lottie.play();
});
```

neat!
