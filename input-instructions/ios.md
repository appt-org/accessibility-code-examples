# Input instructions - iOS

On iOS, we recommend using an [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel) to indicate an error. The error message should also be posted to assistive technologies by using an [`accessibility announcement`](../Techniques/accessibility-announcement.md).

You could also use a third party library to displaying instructions. Unfortunately, accessibility is often not considered in the implementations.

```swift
helpLabel.isHidden = false
helpLabel.text = "Your password should be at least 8 characters."
```
