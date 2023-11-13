# Dark mode - iOS

On iOS, you can detect dark mode by checking if the [`userInterfaceStyle`](https://developer.apple.com/documentation/uikit/uitraitcollection/1651063-userinterfacestyle) has been set to [`.dark`](https://developer.apple.com/documentation/uikit/uiuserinterfacestyle/dark).

You can provide dark mode resources to let iOS automatically use the right resources. For example, inside `Assets.xcassets` you can add a `Dark` version for colors and images.

```swift
func isInDarkMode() -> Bool{
    if #available(iOS 12.0, *) {
        if UIScreen.main.traitCollection.userInterfaceStyle == .dark {
            return true
        }
    }
    return false
}
```
