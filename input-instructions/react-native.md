# Input instructions - React Native

In React Native, there is no default component to combine an input field with a label. We recommend combining [`Text`](https://reactnative.dev/docs/text) with a [`TextInput`](https://reactnative.dev/docs/textinput) component.

You can also use a package for displaying instructions, such as [React Native Paper](https://callstack.github.io/react-native-paper/index.html). This package includes a [`HelperText`](https://callstack.github.io/react-native-paper/docs/components/HelperText/) component which can be used for displaying instructions. The type should be set to `info` for instructions.

```jsx
<Text>Your password should be at least 8 characters.</Text>

<View>
  <TextInput label="Password" value={text} onChangeText={onChangeText} />
  <HelperText type="info">
    Your password should be at least 8 characters.
  </HelperText>
</View>
```
