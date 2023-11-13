# Reflow - React Native

In React Native, your elements should be placed inside a scrollable layout, such as [`ScrollView`](https://reactnative.dev/docs/scrollview). If the elements don't fit, the view becomes scrollable over the vertical axis so the user can still reach them. Ideally scrolling is only necessary in one direction.

```jsx
<ScrollView>
    <Text>
        Content should scroll!
    </Text>
</ScrollView>
```
