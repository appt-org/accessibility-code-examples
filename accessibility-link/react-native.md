# Accessibility link - React Native

In React Native, links should have their [`accessibilityRole`](https://reactnative.dev/docs/accessibility#accessibilityrole) set to `link`. You can use  [`accessibilityLabel`](https://reactnative.dev/docs/accessibility#accessibilitylabel) or [`accessibilityHint`](https://reactnative.dev/docs/accessibility#accessibilityhint) to provide additional context.

To create text links, you can embed a [`Text`](https://reactnative.dev/docs/text) component inside a [`Pressable`](https://reactnative.dev/docs/pressable) component.

The [`Linking API`](https://reactnative.dev/docs/linking) can be used to open links.

```jsx
<Pressable
  onPress={async () => {
    const supported = await Linking.canOpenURL(url);
    if (supported) {
      await Linking.openURL(url);
    }
  }}
  accessibilityRole="link"
  accessibilityLabel="Appt"
  accessibilityHint="External link"
>
  <Text>Appt</Text>
</Pressable>
```
