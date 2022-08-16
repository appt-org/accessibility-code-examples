# Set accessibility name

The accessibility name is the name of a user interface element. It is used by assistive technologies to inform users about ways to interact with your app.

In mobile apps, an `accessibility name` is usually the same as the `accessibility label`.

See [set accessibility label](set-accessibility-label.md) for more information about setting an accessibility label.

## Android

Android uses the [`contentDescription`](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) property as accessibility name.

```kotlin
element.contentDescription = "Appt"
```

## iOS

iOS uses the [accessibilityLabel](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619577-accessibilitylabel) property as accessibility name.

```swift
element.accessibilityLabel = "Appt"
```

## Flutter

Flutter uses the [`label`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/label.html) property provided by the [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) widget as accessibility name.

```dart
Semantics(
  label: 'Appt',
  child: Widget();
);
```

## React Native

React Native uses the [`accessibilityLabel`](https://reactnative.dev/docs/accessibility#accessibilitylabel) prop as accessibility name.

```jsx
<Pressable 
  accessibilityLabel="Appt" />
```

## Xamarin

Xamarin uses the [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) property as accessibility name.

```xml
<Image 
  AutomationProperties.Name="Appt" />
```
