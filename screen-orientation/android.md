# Screen orientation - Android

On Android, make sure that the [`android:screenOrientation`](https://developer.android.com/guide/topics/manifest/activity-element#screen) attribute is not used anywhere.

Open Android Studio and press the Shift key twice to open the search dialog. Search for _“android:screenOrientation”_. In case there are search results, remove the attribute.

You probably need to make additional code adjustments to make sure the all orientations are working as intended.

To listen to orientation changes, add [`android:configChanges="orientation"`](https://developer.android.com/guide/topics/manifest/activity-element#config) to your manifest. Then, override the [`onConfigurationChanged`](https://developer.android.com/reference/android/app/Activity#onConfigurationChanged(android.content.res.Configuration)) to receive configuration notifications. Use the [`orientation`](https://developer.android.com/reference/android/content/res/Configuration#orientation) property of the [`Configuration`](https://developer.android.com/reference/android/content/res/Configuration) object to check the new orientation.

```xml
<activity
    android:name=".ApptActivity"
    android:screenOrientation="portrait" <!-- Remove -->
    android:configChanges="orientation" <!-- Add -->
</activity>
```

```kotlin
override fun onConfigurationChanged(newConfig: Configuration) {
    super.onConfigurationChanged(newConfig)

    when (newConfig.orientation) {
        Configuration.ORIENTATION_PORTRAIT -> {
            // Portrait logic
        }
        Configuration.ORIENTATION_LANDSCAPE -> {
            // Landscape logic
        }
        else -> {
            // Ignored
        }
    }
}
```
