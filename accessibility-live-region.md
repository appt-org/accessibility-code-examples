# Accessibility live region

A live region allows users of assistive technologies to receive updates whenever important information on the screen changes.

## WCAG

Relates to 3.3.1, 4.1.3

## Android

On Android, a live region can be set by using the convience method [`setAccessibilityLiveRegion`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityLiveRegion(android.view.View,int)) of [`ViewCompat`](https://developer.android.com/reference/androidx/core/view/ViewCompat). To interrupt ingoing speech, also known as being assertive, use [`ACCESSIBILITY_LIVE_REGION_ASSERTIVE`](https://developer.android.com/reference/kotlin/androidx/core/view/ViewCompat#ACCESSIBILITY_LIVE_REGION_ASSERTIVE()). To wait for ongoing speech, also known as being polite, use [`ACCESSIBILITY_LIVE_REGION_POLITE`](https://developer.android.com/reference/kotlin/androidx/core/view/ViewCompat#ACCESSIBILITY_LIVE_REGION_POLITE()).

```kotlin
// Interrupt ongoing speech
ViewCompat.setAccessibilityLiveRegion(view, ViewCompat.ACCESSIBILITY_LIVE_REGION_ASSERTIVE)

// Wait for ongoing speech
ViewCompat.setAccessibilityLiveRegion(view, ViewCompat.ACCESSIBILITY_LIVE_REGION_POLITE)
```

## iOS

On iOS, the closest thing to live regions are elements with the [`updatesFrequently`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620187-updatesfrequently) trait. When an element is focused, label and value changes are announced periodically.

You can replicate a live region by posting accessibility announcements. To replicate 'polite' behavior, you can set [`accessibilitySpeechQueueAnnouncement`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/2865770-accessibilityspeechqueueannounce) to `false`. To be 'asssertive', set the value to `true`.

For even more advanced behavior, you can use act on [`announcementDidFinishNotification`](https://developer.apple.com/documentation/uikit/uiaccessibility/1620202-announcementdidfinishnotificatio) events.

```swift
// Periodic announcements (only on focus!)
element.accessibilityTraits = .updatesFrequently

// Replicate live region
let message = NSAttributedString(
    string: "Appt live region", 
    attributes: [.accessibilitySpeechQueueAnnouncement: true]
)
UIAccessibility.post(notification: .announcement, argument: message)
```

## Flutter

On Flutter, the [`liveRegion`](https://api.flutter.dev/flutter/semantics/SemanticsConfiguration/liveRegion.html) property can be used in [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) to indicate a live region. By default, the live region is `polite`: it queues announcements.

```dart
Semantics(
  liveRegion: true,
  child: Text('Appt live region')
);
```

## React Native

On React Native, the [`accessibilityLiveRegion`](https://reactnative.dev/docs/accessibility#accessibilityliveregion-android) prop can be used to indicate a live region. The value can be set to `asssertive` to interrupt ongoing speech to for immediate announcements on change. The `polite` value can be used to queue announcements. The `none` value can be used to disable announcements on change.

```jsx
<Text accessibilityLiveRegion="assertive|polite|none">
  Appt live region
</Text>
```

## Xamarin

Xamarin Forms does not have built-in support to indicate an accessibility live region. By using [`Effects`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/effects/introduction) it is possible to implement platform specific behaviour. The [`A11YEffect`](https://github.com/appt-org/accessibility-code-examples/blob/main/Xamarin/en/A11yEffect.md), [`A11YEffect for Android`](https://github.com/appt-org/accessibility-code-examples/blob/main/Xamarin/en/A11yEffect_Android.md) and [`A11YEffect for iOS`](https://github.com/appt-org/accessibility-code-examples/blob/main/Xamarin/en/A11yEffect_iOS.md) files show how to implement an `effect` to replicate an accessibility live region.

```xml
<controls:CustomFontLabel
    effects:A11YEffect.ControlType="{OnPlatform iOS=LiveUpdate, Android=LiveUpdate}" />
```
