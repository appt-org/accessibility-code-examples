# Accessibility value - React Native

In React Native you can use the [`accessibilityValue`](https://reactnative.dev/docs/accessibility#accessibilityvalue) and [`accessibilityState`](https://reactnative.dev/docs/accessibility#accessibilitystate) props to set an accessibility value. The `accessibilityValue` indicates the current value of a component. You can indicate a range, using `min`, `max`, and `no`, or text using `text`. The `accessibilityState` indicates the current state of a component, for example `disabled` or `checked`.

```jsx
<View
  accessibilityValue={{min: 0, max: 100, now: 50}}
  accessibilityState="busy" />

<View 
  accessibilityValue={{text: "Custom"}}
  accessibilityState="disabled" />
```
