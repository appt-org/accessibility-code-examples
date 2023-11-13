# Accessibility dialog - iOS

On iOS, you can [show alerts](https://developer.apple.com/design/human-interface-guidelines/ios/views/alerts/) by using [`UIAlertController`](https://developer.apple.com/documentation/uikit/uialertcontroller). Set the `style` to [`alert`](https://developer.apple.com/documentation/uikit/uialertcontroller/style/alert) to display a  dialog. You should always add a close action in the [`cancel`](https://developer.apple.com/documentation/uikit/uialertaction/style/cancel) style. The focus of assistive technologies is automatically trapped inside the alert while it's visible.

```swift
let alert = UIAlertController(
  title: "Confirm Appt membership?", 
  message: "Your bank account will be billed.", 
  preferredStyle: .alert
)

alert.addAction(UIAlertAction(title: "Proceed", style: .default, handler: { action in
  // Proceed
}))

alert.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: { action in
  // Cancel
}))

present(alert, animated: true)
```
