# Accessibility dialog - React Native

In React Native, you can use [`Alert`](https://reactnative.dev/docs/alert) to show a dialog. On [Android](https://reactnative.dev/docs/alert#android) you can add a neutral, negative and positive button, this is based on the amount of buttons that are set. On iOS it's possible to set the [AlertButtonStyle](https://reactnative.dev/docs/alert#alertbuttonstyle-ios) for each button. You should always include a button to close the dialog. The focus of assistive technologies is automatically trapped inside the dialog while it's visible.

```jsx
Alert.alert(
  "Confirm Appt membership?",
  "Your bank account will be billed.",
  [
    {
      text: "Cancel",
      onPress: () => {
        // Cancel
      },
      style: "cancel"
    },
    {
      text: "Proceed",
      onPress: () => {
        // Proceed
      },
    },
  ],
  {
      cancelable: true,
      onDismiss: () => console.log("Dismissed alert"),
  }
);
```
