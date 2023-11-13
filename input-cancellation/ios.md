# Input cancellation - iOS

On iOS, you should avoid using [`touchesBegan`](https://developer.apple.com/documentation/uikit/uiresponder/1621142-touchesbegan) or [`UIControlEventTouchDown`](https://developer.apple.com/documentation/uikit/uicontrolevents/uicontroleventtouchdown) because users will not be able to cancel their interaction. Actions should only be activated through `up` events. Use a [`UITapGestureRecognizer`](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer) instead, because it has built-in support for cancellation.

```swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
    // Use UITapGestureRecognizer instead
}
```
