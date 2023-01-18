# Bold text

Apps should use bold text when users have indicated this as a preference  in the system settings. Turning on bold text improves the contrast of the letters against the background, making the text easier to read. This is vital if you are visually impaired, but it can also be useful if you need reading glasses.

## WCAG

Relates to 1.4.12

## Android

Android 12 has added the [`fontWeightAdjustment`](https://developer.android.com/reference/android/content/res/Configuration#fontWeightAdjustment) property. The property returns an integer between `1` and `1000`, which indicates the current user preference for increasing font weight. The constant [`FontStyle.FONT_WEIGHT_BOLD`](https://developer.android.com/reference/android/graphics/fonts/FontStyle#FONT_WEIGHT_BOLD) has a value of `700`.

```kotlin
fun Context.prefersBoldFont(): Boolean {
    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.S) {
        return false
    }
    return resources.configuration.fontWeightAdjustment >= FontStyle.FONT_WEIGHT_BOLD
}
```

## iOS

On iOS, the [`isBoldTextEnabled`](https://developer.apple.com/documentation/uikit/uiaccessibility/1615156-isboldtextenabled) property of [`UIAccessibility`](https://developer.apple.com/documentation/objectivec/nsobject/uiaccessibility) can be used to check whether the user prefers bold text.

```swift
if UIAccessibility.isBoldTextEnabled {
    // Use bold text
}
```

## Flutter

With Flutter, the [`boldText`](https://api.flutter.dev/flutter/dart-ui/AccessibilityFeatures/boldText.html) property of [`AccessibilityFeatures`](https://api.flutter.dev/flutter/dart-ui/AccessibilityFeatures-class.html) can be used to check whether the user prefers bold text.

```dart
if (window.accessibilityFeatures.boldText) {
    // Use bold text
}
```

## React Native

On React Native, the [`isBoldTextEnabled()`](https://reactnative.dev/docs/next/accessibilityinfo#isboldtextenabled-ios) method of [`AccessibilityInfo`](https://reactnative.dev/docs/next/accessibilityinfo) can be used to check whether the user prefers bold text.

Note: it only checks the preference on iOS. Android is not yet supported.

```jsx
import { AccessibilityInfo } from "react-native";

if (AccessibilityInfo.isBoldTextEnabled()) {
    // Use bold text
}
```

## Xamarin

Xamarin does not expose a property which indicates a preference for bold text.

```xml
Not available, contribute!
```
