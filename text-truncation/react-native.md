# Text truncation - React Native

In React Native, you can avoid text truncation by removing all instances of [`numberOfLines`](https://reactnative.dev/docs/text#numberoflines) from you rapp.

```jsx
<Text numberOfLines="{REMOVE}">
    Avoid text truncation
</Text>
```
