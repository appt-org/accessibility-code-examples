# Element identification - React Native

In React Native, you should create custom `Components` to re-use functionality on multiple screens.

When using icons, use the search function of your `IDE` to check all instances. The icon should have the same `accessibility label` on each screen, and the functionality should also be the same.

For example, when using a cross icon for closing a screen, make sure the label is 'Close' on all screens, and check that it always closes a screen.

```jsx
const CloseButton = () => <Pressable
  accessibilityLabel="Close screen"
>
  <Image
    source={require("icon-close.png")}
  />
</Pressable>
```
