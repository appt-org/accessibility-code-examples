# Accessibility language - iOS

On iOS, the [`accessibilitySpeechLanguage`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1620188-accessibilityspeechlanguage) key of [`NSAttributedString`](https://developer.apple.com/documentation/foundation/nsattributedstring) can be used to speak content in a specific language. Multiple `NSAttributedString`'s can be embedded inside a [`NSMutableAttributedString`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring) to speak content in multiple languages.

In addition, the [`accessibilityLanguage`](https://developer.apple.com/documentation/objectivec/nsobject/1615192-accessibilitylanguage) attribute of the [`UIAccessibility`](https://developer.apple.com/documentation/objectivec/nsobject/uiaccessibility) protocol can be used to set a single language for an element. Many objects implement this protocol, such as [`UIApplication`](https://developer.apple.com/documentation/uikit/uiapplication/) and [`UIView`](https://developer.apple.com/documentation/uikit/uiview/).

```swift
element.attributedText = NSAttributedString(
    string: "Appt", 
    attributes: [.accessibilitySpeechLanguage: "nl_NL"]
)

application.accessibilityLanguage = "nl_NL"
view.accessibilityLanguage = "nl_NL"
```
