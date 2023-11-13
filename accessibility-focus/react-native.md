# Accessibility focus - React Native

In React Native you can move accessibility focus by using the [`setAccessibilityFocus`](https://reactnative.dev/docs/accessibilityinfo#setaccessibilityfocus) method from the [`AccessibilityInfo class`](https://reactnative.dev/docs/accessibilityinfo). This method requires a `reactTag`, which you can find by calling the `findNodeHandle` method.

```tsx
function Component() {
  const ref = useRef(null);
  
  function setFocus() {
    const reactTag = findNodeHandle(ref.current);
    
    if (reactTag) {
      AccessibilityInfo.setAccessibilityFocus(reactTag);
    }
  }

  return <View ref={ref} accessible accessibilityLabel="Modal" />
};
```
