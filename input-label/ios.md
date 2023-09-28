On iOS, there is no attribute to link a label to an input field. We recommend combining [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) with a [`UITextField`](https://developer.apple.com/documentation/uikit/uitextfield). Set `isAccessibilityElement` to `false` for the label, and set the text of the label as `accessibilityLabel` for the field.

```swift
label.text = "Name"
label.isAccessibilityElement = false
field.accessibilityLabel = label.text
```
