# Input predictable - iOS

With iOS, be careful when using [`UITextFieldDelegate`](https://developer.apple.com/documentation/uikit/uitextfielddelegate) methods. Do not trigger a change of context when text changes.

```swift
extension ApptViewController: UITextFieldDelegate {
  func textField(_ textField: UITextField,
                  shouldChangeCharactersIn range: NSRange,
                  replacementString string: String) -> Bool {
      // Do not change context
      return true
  }
}
```
