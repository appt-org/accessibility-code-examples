# Reduced animations

Content which conveys a sense of motion can be a barrier for users. Certain groups, particularly those with attention deficit disorders, find moving content distracting, making it difficult for them to concentrate on other parts of your app. You should provide functionality to pause, stop or hide content which moves, blinks or scrolls automatically.

## WCAG

Relates to 2.2.2

## Android

On Android, you should provide buttons to pause, stop or hide content. You could use the [`ANIMATOR_DURATION_SCALE`](https://developer.android.com/reference/android/provider/Settings.Global#ANIMATOR_DURATION_SCALE) and/or [`TRANSITION_ANIMATION_SCALE`](https://developer.android.com/reference/android/provider/Settings.Global#TRANSITION_ANIMATION_SCALE) preferences to check if animations should be disabled. If either value is `zero`, you could choose to disable (non-essential) animations in your app.

```kotlin
val duration = Settings.Global.getFloat(
    context.getContentResolver(), 
    Settings.Global.ANIMATOR_DURATION_SCALE, 
    1f
)

val transition = Settings.Global.getFloat(
    context.getContentResolver(), 
    Settings.Global.TRANSITION_ANIMATION_SCALE, 
    1f
)

if (duration == 0f || transition == 0f) {
    // Disable animations
}
```

## iOS

On iOS, you can read the [`UIAccessibility.isReduceMotionEnabled`](https://developer.apple.com/documentation/uikit/uiaccessibility/1615133-isreducemotionenabled) property. If the value is `true`, you could choose to disable (non-essential) animations in your app. You can do this, for example, with the [`setAnimationsEnabled`](https://developer.apple.com/documentation/uikit/uiview/1622420-setanimationsenabled) method.

```swift
if UIAccessibility.isReduceMotionEnabled {
    UIView.setAnimationsEnabled(false)
}
```

## Flutter

With Flutter, you can use [`MediaQuery.of(context)`](https://api.flutter.dev/flutter/widgets/MediaQuery/of.html) to retrieve the value of [`disableAnimations`](https://api.flutter.dev/flutter/widgets/MediaQueryData/disableAnimations.html). If the value is `true`, you could choose to disable (non-essential) animations in your app.

```dart
if (MediaQuery.of(this).disableAnimations) {
    // Disable animations
}
```

## React Native

In React Native, you can use [`AccessibilityInfo`](https://reactnative.dev/docs/accessibilityinfo) to check get the value of [`isReduceMotionEnabled`](https://reactnative.dev/docs/accessibilityinfo#isreducemotionenabled). If the value is `true`, you could choose to disable (non-essential) animations in your app.

```jsx
import { AccessibilityInfo } from "react-native";

if (AccessibilityInfo.isReduceMotionEnabled()) {
    // Disable animations
}
```

## Xamarin

Xamarin does not expose a property which indicates a preference for reduced motion.

```xml
Not available, contribute!
```
