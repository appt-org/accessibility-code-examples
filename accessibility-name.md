# Accessibility name

All interactive elements must have an accessibility name. The accessibility name is used by assistive technologies to inform users about the ways to interact with your app.

For apps, the `accessibility name` is usually equal to the `accessibility label`. See [accessibility label](accessibility-label.md) for more ways of setting an accessibility label.

## WCAG

Relates to 2.5.3, 4.1.2

## Android

On Android, the [`contentDescription`](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) property is used as accessibility name.

```kotlin
element.contentDescription = "Appt"
```

## iOS

On iOS, [`accessibilityLabel`](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619577-accessibilitylabel) property is used as accessibility name.

```swift
element.accessibilityLabel = "Appt"
```

## Flutter

In Flutter, the [`semanticsLabel`](https://api.flutter.dev/flutter/widgets/Text/semanticsLabel.html) property is used as accessibility name.

```dart
Control(
  semanticsLabel: 'Appt'
);
```

## React Native

In React Native, the [`accessibilityLabel`](https://reactnative.dev/docs/accessibility#accessibilitylabel) prop is used accessibility name.

```jsx
<Control 
  accessibilityLabel="Appt" />
```

## Xamarin

In Xamarin, the  [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) property is used as accessibility name.

```xml
<Control 
  AutomationProperties.Name="Appt" />
```
