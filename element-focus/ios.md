# Element focus change - iOS

On iOS, you can use the [`UIAccessibilityFocus`](https://developer.apple.com/documentation/objectivec/nsobject/uiaccessibilityfocus) protocol to listen to focus changes. The [`accessibilityElementDidBecomeFocused`](https://developer.apple.com/documentation/objectivec/nsobject/1615183-accessibilityelementdidbecomefoc) method is called whenever an element receives focus.

Be careful when using the `accessibilityElementDidBecomeFocused` method: do not trigger any context change because they might confuse users.

```swift
class View: UIView {
    
    override open func accessibilityElementDidBecomeFocused() {
        // Do not change context
    }
}
```
