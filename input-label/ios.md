# Input label - iOS

On iOS, there is no attribute to link a label to an input field. We recommend combining [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) with a [`UITextField`](https://developer.apple.com/documentation/uikit/uitextfield) or [`UITextView`](https://developer.apple.com/documentation/uikit/uitextview).

Set the `accessibilityLabel` of the field to the text of the label.

```swift
label.text = "Name"
field.accessibilityLabel = label.text
```
