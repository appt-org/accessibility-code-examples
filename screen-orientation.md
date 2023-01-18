# Screen orientation

Apps should adapt to the preferred display orientation of the user. Most apps restrict the screen to portrait orientation, but they should also support landscape orientation. Some users have their devices mounted in a fixed orientation (e.g. on the arm of a wheelchair). Therefore, apps need to support both orientations.

## WCAG

Relates to 1.3.4

## Android

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

## iOS

On iOS, make sure all [`UIInterfaceOrientationMask`](https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask) values are used for the [`UISupportedInterfaceOrientations`](https://developer.apple.com/documentation/bundleresources/information_property_list/uisupportedinterfaceorientations) key inside the `Info.plist` file.

To listen to orientation changes, subscribe to [`orientationDidChangeNotification`](https://developer.apple.com/documentation/uikit/uidevice/1620025-orientationdidchangenotification). Check the device orientation using [`UIDevice.current.orientation`](https://developer.apple.com/documentation/uikit/uidevice/1620053-orientation).

```xml
<key>UISupportedInterfaceOrientations</key>
<array>
    <string>UIInterfaceOrientationPortrait</string>
    <string>UIInterfaceOrientationLandscapeLeft</string>
    <string>UIInterfaceOrientationLandscapeRight</string>
    <string>UIInterfaceOrientationPortraitUpsideDown</string>
</array>
```

```swift
private var subscriptions = Set<AnyCancellable>()

override func viewDidLoad() {
    super.viewDidLoad()

    NotificationCenter
        .default
        .publisher(for: UIDevice.orientationDidChangeNotification)
        .sink { [weak self] _ in
            if (UIDevice.current.orientation.isLandscape) {
                // Landscape logic
            } else {
                // Portrait logic
            }
    }
    .store(in: &subscriptions)
}
```

## Flutter

With Flutter, multiple screen orientations are enabled by default.

Orientation can be locked by using the [`setPreferredOrientations`](https://api.flutter.dev/flutter/services/SystemChrome/setPreferredOrientations.html) method of [`SystemChrome`](https://api.flutter.dev/flutter/services/SystemChrome-class.html). Make sure to pass all [`DeviceOrientation`](https://api.flutter.dev/flutter/services/DeviceOrientation.html) values, or simply remove the code from your app.

By using an [`OrientationBuilder`](https://api.flutter.dev/flutter/widgets/OrientationBuilder-class.html) it is possible to make adjustments based on the orientation of the screen.

```dart
// Allow all orientations
SystemChrome.setPreferredOrientations([
  DeviceOrientation.portraitUp,
  DeviceOrientation.portraitDown,
  DeviceOrientation.landscapeRight,
  DeviceOrientation.landscapeLeft
]);

// Listen to orientation changes
OrientationBuilder(
  builder: (context, orientation) {
    return GridView.count(
      // Grid with 2 columns in portrait and 3 columns in landscape
      crossAxisCount: orientation == Orientation.portrait ? 2 : 3,
    );
  },
),
```

## React Native

In React Native, multiple screen orientations are enabled by default. Locking screen orientation is handled in native code:

- For Android, remove instances of the `android:screenOrientation` attribute.
- For iOS, check if 4 orientations have been added to `UISupportedInterfaceOrientations`.

You can use the [`Dimensions`](https://reactnative.dev/docs/dimensions) API to listen to orientation changes.

```jsx
Dimensions.addEventListener('change', () => {
    this.setState({
        orientation: Platform.isPortrait() ? 'portrait' : 'landscape'
    });
});
```

## Xamarin

When using Xamarin.Forms, [device orientation](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/layouts/device-orientation) is set at the project level.

- For Android: open `MainActivity.cs` and decorate the `MainActivity` class with `[Activity (ScreenOrientation = ScreenOrientation.FullUser)]`.
- For iOS: open `Info.plist` and check all `Device Orientation` checkboxes.

You can listen to orientation changes by using the [`DeviceDisplay`](https://learn.microsoft.com/en-us/xamarin/essentials/device-display?context=xamarin%2Fxamarin-forms&tabs=android) class included in [Xamarin.Essentials](https://learn.microsoft.com/en-us/xamarin/essentials/).

```csharp
public class OrientationChanges
{
    public OrientationChanges()
    {
        // Subscribe to changes of screen metrics
        DeviceDisplay.MainDisplayInfoChanged += OnMainDisplayInfoChanged;
    }

    void OnMainDisplayInfoChanged(object sender, DisplayInfoChangedEventArgs  e)
    {
        // Process changes
        var displayInfo = e.DisplayInfo;
    }
}
```
