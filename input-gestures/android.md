# Input gestures - Android

On Android, the [`GestureDetector`](https://developer.android.com/reference/android/view/GestureDetector) and  [`OnGestureListener`](https://developer.android.com/reference/android/view/GestureDetector.OnGestureListener) objects are a common way to detect gestures.

A gesture should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```kotlin
val scaleGestureDetector = ScaleGestureDetector(
    this,
    object : ScaleGestureDetector.SimpleOnScaleGestureListener() {
        override fun onScale(detector: ScaleGestureDetector): Boolean {
            // Provide alternative
            return super.onScale(detector)
        }
    }
)

view.setOnTouchListener { _, event ->
    scaleGestureDetector.onTouchEvent(event)
}
```
