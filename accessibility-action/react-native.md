# Accessibility action - React Native

In React Native, you can add [`accessibility actions`](https://reactnative.dev/docs/accessibility#accessibility-actions) using the `accessibilityActions` and `onAccessibilityAction` properties.

```jsx
<View
  accessible
  accessibilityRole="adjustable"
  accessibilityActions={[{name: 'increment', label: 'Increment'}]}
  onAccessibilityAction={event => {
    if (event.nativeEvent.actionName === 'increment') {
      handleIncrement();
    }
  }}
/>
```
