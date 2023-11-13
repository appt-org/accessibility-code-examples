# Descriptive headers - Android

On Android, headers created with [`TextView`](https://developer.android.com/reference/android/widget/TextView) can be changed with the [`setText`](https://developer.android.com/reference/android/widget/TextView#setText(java.lang.CharSequence)) method.

```kotlin
header.text = "Descriptive header"
ViewCompat.setAccessibilityHeading(header, true)
```
