# Accessibility order - Android

On Android, you can set the accessibility order in XML, or modify the accessibility order in code. You can use the [`android:accessibilityTraversalAfter`](https://developer.android.com/reference/android/view/View#attr_android:accessibilityTraversalAfter) and [`android:accessibilityTraversalBefore`](accessibilityTraversalBefore) properties in XML. Or you can use the [`setAccessibilityTraversalBefore`](https://developer.android.com/reference/android/view/View#setAccessibilityTraversalBefore(int)) and [`setAccessibilityTraversalAfter`](https://developer.android.com/reference/android/view/View#setAccessibilityTraversalAfter(int)) methods in code.

```xml
<TextView
    android:id="@+id/header" />
<RecyclerView
    android:id="@+id/list"
    android:accessibilityTraversalAfter="@id/description" />
<TextView
    android:id="@+id/description"
    android:accessibilityTraversalBefore="@id/header" />
```

```kotlin
header.setAccessibilityTraversalBefore(R.id.description)
list.setAccessibilityTraversalAfter(R.id.description)
```
