# Accessibility action - Android

On Android, you can add custom actions for assistive technologies using the [`ViewCompat.addAccessibilityAction`](https://developer.android.com/reference/androidx/core/view/ViewCompat#addAccessibilityAction(android.view.View,java.lang.CharSequence,androidx.core.view.accessibility.AccessibilityViewCommand)) helper method.

You can also use the [`addAction`](https://developer.android.com/reference/kotlin/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#addAction(androidx.core.view.accessibility.AccessibilityNodeInfoCompat.AccessibilityActionCompat)) method of [`AccessibilityNodeInfoCompat`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat) to override labels for default actions.

```kotlin
// Add custom action
ViewCompat.addAccessibilityAction(view, "Add bookmark") { view, arguments ->
    // Bookmark logic
    true
}

// Override click action label
ViewCompat.setAccessibilityDelegate(view, new AccessibilityDelegateCompat() {
    @Override
    public void onInitializeAccessibilityNodeInfo(
        View host,
        AccessibilityNodeInfoCompat info)
    {
        super.onInitializeAccessibilityNodeInfo(host, info)
        AccessibilityActionCompat action = new AccessibilityActionCompat(
            AccessibilityNodeInfoCompat.ACTION_CLICK,
            "Add bookmark"
        )
        info.addAction(action)
    }
})
```
