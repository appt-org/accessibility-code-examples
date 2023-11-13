# Accessibility live region - Android

On Android, a live region can be set by using the convience method [`setAccessibilityLiveRegion`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityLiveRegion(android.view.View,int)) of [`ViewCompat`](https://developer.android.com/reference/androidx/core/view/ViewCompat). To interrupt ingoing speech, also known as being assertive, use [`ACCESSIBILITY_LIVE_REGION_ASSERTIVE`](https://developer.android.com/reference/kotlin/androidx/core/view/ViewCompat#ACCESSIBILITY_LIVE_REGION_ASSERTIVE()). To wait for ongoing speech, also known as being polite, use [`ACCESSIBILITY_LIVE_REGION_POLITE`](https://developer.android.com/reference/kotlin/androidx/core/view/ViewCompat#ACCESSIBILITY_LIVE_REGION_POLITE()).

```kotlin
// Interrupt ongoing speech
ViewCompat.setAccessibilityLiveRegion(view, ViewCompat.ACCESSIBILITY_LIVE_REGION_ASSERTIVE)

// Wait for ongoing speech
ViewCompat.setAccessibilityLiveRegion(view, ViewCompat.ACCESSIBILITY_LIVE_REGION_POLITE)
```
