# Accessibility announcement - Android

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
