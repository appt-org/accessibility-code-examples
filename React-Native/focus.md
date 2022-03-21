# Set accessibility focus

When you open a new element on top of your current content, for example a modal, you want to shift focus so the user can navigate through the content of this element. In React Native you can use the [`setAccessibilityFocus`](https://reactnative.dev/docs/accessibilityinfo#setaccessibilityfocus) method from the AccessibilityInfo API. You can find the `reactTag` to pass to the `setAccessibilityFocus` method by calling `findNodeHandle`.

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