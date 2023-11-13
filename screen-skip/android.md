# Skip content - Android

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
