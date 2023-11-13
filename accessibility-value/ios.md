# Accessibility value - iOS

On iOS, you can set an accessibility value with the [`accessibilityValue`](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619583-accessibilityvalue) or [`accessibilityAttributedValue`](https://developer.apple.com/documentation/objectivec/nsobject/2866105-accessibilityattributedvalue/) property.

When using the semantically correct element, you usually do not need to modify the `accessibilityValue`. For example, a [`UISwitch`](https://developer.apple.com/documentation/uikit/uiswitch) sets the `accessibilityValue` to `selected` or `not selected` and a [`UISlider`](https://developer.apple.com/documentation/uikit/uislider) sets the `accessibilityValue` to the current value. If the default value is incorrect or unclear, you can override the value manually.

```swift
element.accessibilityValue = "Custom"
```
