# Accessibility value - Android

Android has limited support to provide a dedicated accessibility value for assistive technologies. The [`AccessibilityNodeInfoCompat`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat) object contains a couple of methods, such as the [`setChecked`](https://developer.android.com/reference/kotlin/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setchecked) method.

Unfortunately the desired value is often not available. If your desired value is not included, you can append it to the [`contentDescription`](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) attribute.

```kotlin
ViewCompat.setAccessibilityDelegate(
    element,
    object : AccessibilityDelegateCompat() {
        override fun onInitializeAccessibilityNodeInfo(
            host: View,
            info: AccessibilityNodeInfoCompat
        ) {
            super.onInitializeAccessibilityNodeInfo(host, info)
            info.isChecked = true
        }
    }
)

element.contentDescription = "Name (Value)"
```
