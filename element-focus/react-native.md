# Element focus change - React Native

In React Native, you can use the [`onFocus`](https://reactnative.dev/docs/next/textinput#onfocus) method to listen to focus changes. The method is called when the element receives focus.

Be careful when the `onFocus` callback: do not trigger any context change because they might confuse users.

```jsx
<TextInput onFocus={() => {
    // Do not change context
}} />
```
