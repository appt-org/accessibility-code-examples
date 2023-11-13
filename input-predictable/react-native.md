# Input predictable - React Native

In React Native, be careful when using [`onChange`](https://reactnative.dev/docs/next/textinput#onchange) or [`onChangeText`](https://reactnative.dev/docs/textinput#onchangetext) callbacks. Do not trigger a change of context when text changes.

```jsx
<TextInput 
  onChangeText={ /* Do not change context */ }
/>
```
