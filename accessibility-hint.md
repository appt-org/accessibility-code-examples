# Accessibility hint

An accessibility hint helps users to understand what will happen after performing an action. Accessibility hints are announced by the screen reader. Keep in mind that users can turn off accessibility hints. You should therefore not rely on accessibility hints as the sole indicator of what happens. You should also avoid information duplication, e.g. avoid telling users that they can 'double tap to activate'.

## WCAG

Relates to 1.3.3

## Android

On Android, you can use [`setHint`](https://developer.android.com/reference/android/widget/TextView#setHint(int)) to set a hint. Keep in mind that this `hint` is not only used for accessibility, but also shown visually in editable views.

```kotlin
view.hint = "Opens the Appt website"
```

```xml
<Button
    android:hint="Opens the Appt website">
</Button>
```

## iOS

On iOS, you can use the [`accessibilityHint`](https://developer.apple.com/documentation/objectivec/nsobject/1615093-accessibilityhint) property to provide an accessibility hint.

```swift
button.accessibilityHint = "Opens the Appt website"
```

## Flutter

With Flutter, you can set an accessibility hint by using the [`hint`](https://api.flutter.dev/flutter/semantics/SemanticsProperties/hubt.html) property provided by the [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) widget.

```dart
Semantics(
  hint: 'Opens the Appt website'
);
```

## React Native

In React Native you can set an accessibility hint by using the [`accessibilityHint`](https://reactnative.dev/docs/accessibility#accessibilityhint) prop.

```jsx
<Pressable
  accessibilityHint="Opens the Appt website"
/>
```

## Xamarin

In Xamarin Forms you can set an accessibility hint by using the [`AutomationProperties.HelpText`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertieshelptext) property.

```xml
<Button
  AutomationProperties.HelpText="Opens the Appt website" />
```

```csharp
AutomationProperties.SetHelpText(button, "Opens the Appt website");
```
