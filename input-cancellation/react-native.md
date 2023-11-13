# Input cancellation - React Native

In React Native, be careful when using [`PressEvent`](https://reactnative.dev/docs/pressevent). Avoid using events like [`onPressIn`](https://reactnative.dev/docs/pressable#onpressin), because users will not be able to cancel their interaction. Use events like [`onPress`](https://reactnative.dev/docs/pressable#onpressin) instead, because these have built-in support for cancellation.

```jsx
<Pressable
  onPressIn={() => {
    // Use onPress instead
  }}
/>
```
