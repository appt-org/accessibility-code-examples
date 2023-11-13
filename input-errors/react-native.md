# Input errors - React Native

In React Native we recommend using a [`Text`](https://reactnative.dev/docs/text) component to display an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

You can also use a package for displaying errors, such as [React Native Paper](https://callstack.github.io/react-native-paper/index.html). This package includes a [`HelperText`](https://callstack.github.io/react-native-paper/docs/components/HelperText/) component which can be used for displaying errors. The type should be set to `error` for errors.

```jsx
<Text>Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000</Text>

<View>
  <TextInput label="Date of birth" value={text} onChangeText={onChangeText} />
  <HelperText type="error" visible={hasErrors()}>
    Invalid date, must be in the form DD/MM/YYYY, for example, 01/01/2000
  </HelperText>
</View>
```
