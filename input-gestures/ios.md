# Input gestures - iOS

On iOS, the [`UIGestureRecognizer`](https://developer.apple.com/documentation/uikit/uigesturerecognizer) and [`UIGestureRecognizerDelegate`](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate) objects are a common way to detect gestures.

A gesture should not be the only way to trigger actions. Make sure to provide a second way, such as a button, to trigger the same action.

```swift
let gesture = UIPinchGestureRecognizer(
    target: self, 
    action: #selector(onPinch(_:))
)
addGestureRecognizer(gesture)

@objc private func onPinch(_ sender: UIPinchGestureRecognizer) {
    // Provide alternative
  }
}
```
