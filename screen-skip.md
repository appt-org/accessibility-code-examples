# Skip content

It can be helpful for users to skip repeated blocks of content. Most apps have content which appears on multiple screens. It takes longer for users of using assistive technologies to get navigate past repeated content. Adding the ability to skip past repeated content helps these users to navigate quicker.

## WCAG

Relates to 2.4.1

## Android

On Android, skipping content is mostly relevant to [`TalkBack`](https://appt.org/en/docs/android/features/talkback) users. TalkBack includes a `local context menu` which allows users to jump to the following content types:

- Headings
- Links
- Controls
- Text
  - Paragraphs
  - Lines
  - Characters
  - Words

Jumping to `headings` and `links` is used most often.

Provide appropriate accessibility markup to your content by using [`ViewCompat`](https://developer.android.com/reference/androidx/core/view/ViewCompat) and [`AccessibilityNodeInfoCompat`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat).

```kotlin
// Mark headings
ViewCompat.setAccessibilityHeading(heading, true)

// Mark links
ViewCompat.enableAccessibleClickableSpanSupport(link)
```

## iOS

On iOS, skipping content is mostly relevant to [`VoiceOver`](https://appt.org/en/docs/ios/features/voiceover) users. VoiceOver includes a `rotor` which allows users to jump to the following content types:

- Headers
- Links
- Form Controls
- Containers
- Text
  - Lines
  - Characters
  - Words

Jumping to `headers` and `links` is used most often.

Provide appropriate accessibility markup to your content by using [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits).

```swift
header.accessibilityTraits = .header
header.accessibilityTraits = .link
```

## Flutter

In Flutter, skipping content is mostly relevant to [`TalkBack`](https://appt.org/en/docs/android/features/talkback) and [`VoiceOver`](https://appt.org/en/docs/ios/features/voiceover) users. Both screen readers include shortcuts which allows users to jump to content types, such as `headers` and `links`.

Provide appropriate accessibility markup to your content by using [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html).

```dart
Semantics(
  header: true,
  link: true,
  child: Widget(...)
);
```

## React Native

In React Native, skipping content is mostly relevant to [`TalkBack`](https://appt.org/en/docs/android/features/talkback) and [`VoiceOver`](https://appt.org/en/docs/ios/features/voiceover) users. Both screen readers include shortcuts which allows users to jump to content types, such as `headers` and `links`.

Provide appropriate accessibility markup to your content by using [`accessibilityRole`](https://reactnative.dev/docs/accessibility#accessibilityrole).

```jsx
<Pressable 
  accessibilityRole="header|link" />
```

## Xamarin

In Xamarin, skipping content is mostly relevant to [`TalkBack`](https://appt.org/en/docs/android/features/talkback) and [`VoiceOver`](https://appt.org/en/docs/ios/features/voiceover) users. Both screen readers include shortcuts which allows users to jump to content types, such as `headers` and `links`.

Provide appropriate accessibility markup to your content by using [`SemanticEffect`](https://github.com/xamarin/XamarinCommunityToolkit/blob/main/src/CommunityToolkit/Xamarin.CommunityToolkit/Effects/Semantic/SemanticEffect.shared.cs).

```csharp
<controls:CustomFontLabel
    xct:SemanticEffect.HeadingLevel="1"
    xct:SemanticEffect.Description="Link" />
```
