# Reduced animations - Android

On Android, you should provide buttons to pause, stop or hide content. You could use the [`ANIMATOR_DURATION_SCALE`](https://developer.android.com/reference/android/provider/Settings.Global#ANIMATOR_DURATION_SCALE) and/or [`TRANSITION_ANIMATION_SCALE`](https://developer.android.com/reference/android/provider/Settings.Global#TRANSITION_ANIMATION_SCALE) preferences to check if animations should be disabled. If either value is `zero`, you could choose to disable (non-essential) animations in your app.

```kotlin
val duration = Settings.Global.getFloat(
    context.getContentResolver(), 
    Settings.Global.ANIMATOR_DURATION_SCALE, 
    1f
)

val transition = Settings.Global.getFloat(
    context.getContentResolver(), 
    Settings.Global.TRANSITION_ANIMATION_SCALE, 
    1f
)

if (duration == 0f || transition == 0f) {
    // Disable animations
}
```
