# Accessibility focus indicator - Flutter

In Flutter, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings on Android and iOS.

You can change colors based on [`MaterialState`](https://api.flutter.dev/flutter/material/MaterialState.html). For a button, you could add a [`ButtonStyle`](https://api.flutter.dev/flutter/material/ButtonStyle-class.html) to change the color when in [`.focused`](https://api.flutter.dev/flutter/material/MaterialState.html#focused) state.

The code sample below shows how to change the background color of a button on focus.

```dart
TextButton(
  style: ButtonStyle(
    backgroundColor: MaterialStateProperty.resolveWith(getColor),
  ),
  child: Text('Button'),
);

Color? getColor(Set<MaterialState> states) {
  const Set<MaterialState> interactiveStates = <MaterialState>{
    MaterialState.focused,
  };
  if (states.any(interactiveStates.contains)) {
    return Colors.blue;
  }
  return Colors.red;
}
```
