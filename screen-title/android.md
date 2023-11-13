# Screen title - Android

On Android, we recommend using a [`Toolbar`](https://developer.android.com/reference/androidx/appcompat/widget/Toolbar) with an appropriate [`title`](https://developer.android.com/reference/android/app/Activity.html#setTitle(java.lang.CharSequence)) on each screen.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.appt)

    val toolbar = findViewById(R.id.toolbar)
    setSupportActionBar(toolbar)
    title = "Appt homescreen"
}
```
