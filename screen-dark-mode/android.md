# Dark mode - Android

On Android, you can detect dark mode by checking if the [`uiMode`](https://developer.android.com/reference/android/content/res/Configuration#uiMode) configuration contains [`UI_MODE_NIGHT_MASK`](https://developer.android.com/reference/android/content/res/Configuration#UI_MODE_NIGHT_MASK).

By adding `-night` resources to your project you can let Android automatically pick the right resources. For example, add a `colors.xml` file inside a `values-night` folder to specify night mode colors.

```kotlin
fun Context.isInNightMode(): Boolean {
    val nightModeFlags = resources.configuration.uiMode and Configuration.UI_MODE_NIGHT_MASK
    return nightModeFlags == Configuration.UI_MODE_NIGHT_YES
}
```
