# Skip content - iOS

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
