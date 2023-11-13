# Accessibility focus indicator - iOS

On iOS, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings of iOS.

You can override the [`accessibilityElementDidBecomeFocused`](https://developer.apple.com/documentation/objectivec/nsobject/1615183-accessibilityelementdidbecomefoc) and [`accessibilityElementDidLoseFocus`](https://developer.apple.com/documentation/objectivec/nsobject/1615082-accessibilityelementdidlosefocus) methods to listen to focus state changes. By subclassing an element, you can change the colors based on the element state.

The code sample below shows how to change the background color of a button on focus.

```swift
class Button: UIButton {
    
    override open func accessibilityElementDidBecomeFocused() {
        backgroundColor = .focused
    }

    override open func accessibilityElementDidLoseFocus() {
        backgrounColor = .default
    }
}
```
