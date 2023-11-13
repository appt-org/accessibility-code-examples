# Accessibility focus - iOS

On iOS, you can use [`UIAccessibility`](https://developer.apple.com/documentation/objectivec/nsobject/uiaccessibility) to [`post`](https://developer.apple.com/documentation/uikit/uiaccessibility/1615194-post) a notification to move the focus of assistive technologies. Use [`screenChanged`](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/1620198-screenchanged/) when a new view appears that occupies a major portion of the screen. Otherwise, use [`layoutChanged`](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/1620186-layoutchanged) when the layout of current screen changes.

```swift
func focus(_ view: UIView) {
    UIAccessibility.post(notification: .layoutChanged, argument: view)
    UIAccessibility.post(notification: .screenChanged, argument: view)
}
```
