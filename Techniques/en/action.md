# Add accessibility action
## React-Native

In React Native accessibility actions allow an assistive technology to programmatically invoke the actions of a component.
You need to add two properties to the element to support these [`accessibility actions`](https://reactnative.dev/docs/accessibility#accessibility-actions): `accessibilityActions` and `onAccessibilityAction`.

```jsx
<View
  accessible
  accessibilityRole="adjustable"
  accessibilityActions={[{name: 'increment', label: 'Add'}]}
  onAccessibilityAction={event => {
    if (event.nativeEvent.actionName === 'increment') {
      handleIncrement();
    }
  }}
/>
```