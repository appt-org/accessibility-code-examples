# Accessibility group - React Native

In React Native, you can group elements together by using the [`accessible`](https://reactnative.dev/docs/accessibility#accessible) prop. An [`accessibilityLabel`](https://reactnative.dev/docs/accessibility#accessibilitylabel) should be set for grouped elements.

Note: all touchable elements are accessible by default.

```jsx
<View accessible accessibilityLabel="Appt group">
  <Text>Appt</Text>
  <Text>is a platform for accessibility</Text>
</View>
```
