# Accessibility hint - Android

On Android, you can use [`setHint`](https://developer.android.com/reference/android/widget/TextView#setHint(int)) to set a hint. Keep in mind that this `hint` is not only used for accessibility, but also shown visually in editable views.

```kotlin
view.hint = "Opens the Appt website"
```

```xml
<Button
    android:hint="Opens the Appt website">
</Button>
```
