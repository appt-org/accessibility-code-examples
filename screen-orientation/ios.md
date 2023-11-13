# Screen orientation - iOS

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
