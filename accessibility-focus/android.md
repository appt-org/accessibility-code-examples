# Accessibility focus - Android

On Android, you can send an [`AccessibilityEvent`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent) of the type [`TYPE_VIEW_FOCUSED`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#TYPE_VIEW_FOCUSED) to move the focus of assistive technologies to a specific view. The view must be focusable for this event to take effect.

```kotlin
fun focus(view: View) {
    view.sendAccessibilityEvent(AccessibilityEvent.TYPE_VIEW_FOCUSED)
}
```
