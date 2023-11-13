# Reduced animations - iOS

On iOS, you can read the [`UIAccessibility.isReduceMotionEnabled`](https://developer.apple.com/documentation/uikit/uiaccessibility/1615133-isreducemotionenabled) property. If the value is `true`, you could choose to disable (non-essential) animations in your app. You can do this, for example, with the [`setAnimationsEnabled`](https://developer.apple.com/documentation/uikit/uiview/1622420-setanimationsenabled) method.

```swift
if UIAccessibility.isReduceMotionEnabled {
    UIView.setAnimationsEnabled(false)
}
```
