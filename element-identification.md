# Element identification

Functionality that is repeated on multiple screens should use consistent identification. Screen readers users rely heavily on their familiarity with functions that may appear on different screens. If identical functions have different labels on different screens, your app will be considerably more difficult to use. It may also be confusing and increase the cognitive load for people with cognitive limitations.

## WCAG

Relates to 3.2.4

## Android

In Android, you should create custom `Views` to re-use functionality on multiple screens.

When using icons, use the search function of your `IDE` to check all instances. The icon should have the same `accessibility label` on each screen, and the functionality should also be the same.

For example, when using a cross icon for closing a screen, make sure the label is 'Close' on all screens, and check that it always closes a screen.

In Android Studio, you can use the `Find Usages` option to check if resources are used on multiple screens. Go to your `drawable` folder, right click and select the `Find Usages` option. You can also use the shortcut `Option + F7` on Mac, or `Alt + F7` on Windows.

```kotlin
Not available, contribute!
```

## iOS

In iOS, you should create custom `Views` to re-use functionality on multiple screens.

When using icons, use the search function of your `IDE` to check all instances. The icon should have the same `accessibility label` on each screen, and the functionality should also be the same.

For example, when using a cross icon for closing a screen, make sure the label is 'Close' on all screens, and check that it always closes a screen.

In Xcode you can use the shortcut  `Cmd + Shift + F` on Mac, or `Ctrl + Shift + F` on Window  to open the global `Find` function.

```swift
Not available, contribute!
```

## Flutter

In Flutter, you should create custom `Widgets` to re-use functionality on multiple screens.

When using icons, use the search function of your `IDE` to check all instances. The icon should have the same `accessibility label` on each screen, and the functionality should also be the same.

For example, when using a cross icon for closing a screen, make sure the label is 'Close' on all screens, and check that it always closes a screen.

```dart
Not available, contribute!
```

## React Native

In React Native, you should create custom `Components` to re-use functionality on multiple screens.

When using icons, use the search function of your `IDE` to check all instances. The icon should have the same `accessibility label` on each screen, and the functionality should also be the same.

For example, when using a cross icon for closing a screen, make sure the label is 'Close' on all screens, and check that it always closes a screen.

```jsx
const CloseButton = () => <Pressable
  accessibilityLabel="Close screen"
>
  <Image
    source={require("icon-close.png")}
  />
</Pressable>
```

## Xamarin

In Xamarin, you should create custom `Views` to re-use functionality on multiple screens.

When using icons, use the search function of your `IDE` to check all instances. The icon should have the same `accessibility label` on each screen, and the functionality should also be the same.

For example, when using a cross icon for closing a screen, make sure the label is 'Close' on all screens, and check that it always closes a screen.

```csharp
Not available, contribute!
```
