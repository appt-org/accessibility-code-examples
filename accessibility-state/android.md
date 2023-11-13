# Accessibility state - Android

On Android, you can use the [`setAccessibilityDelegate`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityDelegate(android.view.View,androidx.core.view.AccessibilityDelegateCompat)) method of [`ViewCompat`](https://developer.android.com/reference/androidx/core/view/ViewCompat) to get a reference to [`AccessibilityNodeInfoCompat`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat). This object contains many useful accessibility related methods.

You can set an accessibility state by using the [`setStateDescription`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setStateDescription(java.lang.CharSequence)) method. A convenience method is available in `ViewCompat`, which is also named  [`setStateDescription`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setStateDescription(android.view.View,java.lang.CharSequence)).

You can also use the [`setChecked`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setChecked(boolean)) method to indicate a checked state and the [`setSelected`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setSelected(boolean)) method to indicate a selected state.

```kotlin
ViewCompat.setStateDescription(view, "Expanded")

ViewCompat.setAccessibilityDelegate(
    view,
    object : AccessibilityDelegateCompat() {
        override fun onInitializeAccessibilityNodeInfo(
            host: View,
            info: AccessibilityNodeInfoCompat
        ) {
            super.onInitializeAccessibilityNodeInfo(host, info)

            // Custom state
            info.stateDescription = "Expanded"

            // Checked
            info.isChecked = true

            // Selected
            info.isSelected = true
        }
    }
)
```
