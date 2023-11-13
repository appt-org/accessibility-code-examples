# Accessibility focusable - Android

On Android, you can use the [`setImportantForAccessibility`](https://developer.android.com/reference/android/view/View#setImportantForAccessibility(int)) method to set whether assistive technologies can focus on an element. You can also set this property directly in XML by using the [`android:importantForAccessibility`](https://developer.android.com/reference/android/view/View#attr_android:importantForAccessibility) property.

```kotlin
view.importantForAccessibility = View.IMPORTANT_FOR_ACCESSIBILITY_NO
```

```xml
<View
  android:importantForAccessibility="no" />
```
