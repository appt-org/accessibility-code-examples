# Adjustable timing - iOS

On iOS,  third-party code libraries are sometimes used to display a temporary message, also known as a `Toast`. The display duration might be too short for people to read or hear the message.

We recommend showing messages by using an [`UIAlertController`](https://developer.apple.com/documentation/uikit/uialertcontroller). Don't forget to add a close button.

Also check whether [`DispatchQueue`](https://developer.apple.com/documentation/dispatch/dispatchqueue) is used somewhere. If there are time limits, make sure they can be extended.

```swift
let alert = UIAlertController(
  title: nil, 
  message: "Appt", 
  preferredStyle: .alert
)

alert.addAction(UIAlertAction(title: "Close", style: .default, handler: { action in
  // Close
}))

present(alert, animated: true)
```
