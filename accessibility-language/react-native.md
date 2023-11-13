# Accessibility language - React Native

In React Native, there is limited support to change the accessibility language. The [`accessibilityLanguage`](https://reactnative.dev/docs/text#accessibilitylanguage-ios) prop of [`Text`](https://reactnative.dev/docs/text) only works on iOS. Multiple `Text` elements can be combined to speak content in multiple languages.

```jsx
<Text>
  <Text accessibilityLanguage="nl-NL">Appt</Text>
  <Text>is an accessibility platform.</Text>
</Text>
```
