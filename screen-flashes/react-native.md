# Frequent flashes - React Native

In React Native, flashing content might be a result of using [`Animated`](https://reactnative.dev/docs/animated) or [`Timers`](https://reactnative.dev/docs/timers). By default, each animation will take 500 milliseconds. Make sure your animations does not result in more than three flashes per second.

If your app contains any videos, also check if these contain more than three flashes per second.

```jsx
setTimeout(() => {
    // Avoid three flashes per second
}, 500);
```
