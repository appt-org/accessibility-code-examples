# Screen title - iOS

On iOS, we recommend using a [`UINavigationController`](https://developer.apple.com/documentation/uikit/uinavigationcontroller) with an appropriate [`title`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621364-title) on each screen.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    title = "Appt homescreen"
}
```
