# Skip content - Flutter

In Flutter, skipping content is mostly relevant to [`TalkBack`](https://appt.org/en/docs/android/features/talkback) and [`VoiceOver`](https://appt.org/en/docs/ios/features/voiceover) users. Both screen readers include shortcuts which allows users to jump to content types, such as `headers` and `links`.

Provide appropriate accessibility markup to your content by using [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html).

```dart
Semantics(
  header: true,
  link: true,
  child: Widget(...)
);
```
