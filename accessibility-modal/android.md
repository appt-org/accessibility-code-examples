# Accessibility modal - Android

On Android, there is no method to indicate an accessibility modal. However, you can can indicate an accessibility pane by using the [`setPaneTitle`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setPaneTitle(java.lang.CharSequence)) method. `ViewCompat` also contains a convenience method: [`setAccessibilityPaneTitle`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityPaneTitle(android.view.View,java.lang.CharSequence)). Please keep in mind that is focus is not trapped when a pane title has been set.

```kotlin
ViewCompat.setAccessibilityPaneTitle(view, "Appt pane")
```
