# Accessibility announcement

Users of assistive technologies should be made aware of important changes in content through accessibility announcements. What happens next depends on the active assistive technology. The screen reader for example, will read the message aloud.

## WCAG

Relates to 3.3.1, 4.1.3

## Android

On Android, you can post an accessibility message by using the [`AccessibilityManager`](https://developer.android.com/reference/android/view/accessibility/AccessibilityManager) object. Create an [`AccessibilityEvent`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent), set the type to [`AccessibilityEvent.TYPE_ANNOUNCEMENT`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#TYPE_ANNOUNCEMENT) and supply a message.

```kotlin
val type = AccessibilityEventCompat.TYPE_ANNOUNCEMENT

val event = AccessibilityEvent.obtain(type)
event.text.add("Appt announcement")
event.className = Context::class.java.name
event.packageName = packageName

val accessibilityManager = ContextCompat.getSystemService(this, AccessibilityManager::class.java)
accessibilityManager?.sendAccessibilityEvent(event)
```

## iOS

On iOS, you post an accessibility message by using the [`UIAccessibility`](https://developer.apple.com/documentation/uikit/uiaccessibility) object. The [`post`](https://developer.apple.com/documentation/uikit/uiaccessibility/1615194-post) method can be used to post data to assistive technologies. Set the type to [`announcement`](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/1620176-announcement) and supply a `string` argument to announce something.

```swift
UIAccessibility.post(notification: .announcement, argument: "Appt announcement")
```

## Flutter

With Flutter, you can post an accessibility message by using the [`SemanticsService`](https://api.flutter.dev/flutter/semantics/SemanticsService-class.html) object. Use the [`announce`](https://api.flutter.dev/flutter/semantics/SemanticsService/announce.html) method to post an accessibility announcement.

```dart
SemanticsService.announce('Appt announcement', TextDirection.ltr);
```

## React Native

In React Native, you can post an accessibility message by using the [`AccessibilityInfo`](https://reactnative.dev/docs/accessibilityinfo) API. Use the [`announceForAccessibility`](https://reactnative.dev/docs/accessibilityinfo#announceforaccessibility) method to post a message to assistive technologies.

```jsx
AccessibilityInfo.announceForAccessibility('Appt announcement');
```

## Xamarin

Xamarin Forms does not have built-in support for changing accessibility focus.

The [`SemanticExtensions`](https://github.com/xamarin/XamarinCommunityToolkit/blob/main/src/CommunityToolkit/Xamarin.CommunityToolkit/Extensions/Semantic/SemanticExtensions.shared.cs) file inside the [`Xamarin.CommunityToolkit`](https://github.com/xamarin/XamarinCommunityToolkit) contains the `Announce` method. It posts an accessibility announcement on the native platform.

```csharp
SemanticExtensions.Announce("Appt announcement");
```
