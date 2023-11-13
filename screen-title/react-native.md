# Screen title - React Native

In React Native, we recommend using [React Navigation](https://reactnative.dev/docs/navigation) with an appropriate [`title`](https://reactnavigation.org/docs/headers#setting-the-header-title) on each screen.

```jsx
function StackScreen() {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name="Home"
        component={HomeScreen}
        options={{ title: 'Appt homescreen' }}
      />
    </Stack.Navigator>
  );
}
```
