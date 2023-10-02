On iOS, links should contain the [`link`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1535719-link) attribute. This attribute can be added through the [`addAttribute`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring/1417080-addattribute) method of [`NSMutableAttributedString`](https://developer.apple.com/documentation/foundation/nsmutableattributedstring)

To create text links, you can show the `attributed string` by using the the [`attributedText`](https://developer.apple.com/documentation/uikit/uilabel/1620542-attributedtext) property of [`UILabel`](https://developer.apple.com/documentation/uikit/uilabel).

```swift
guard let url = URL(string: "https://appt.org") else { return }
let link = "Appt"

let attributedString = NSMutableAttributedString(string: "Learn more about \(link)")

let range = attributedString.mutableString.range(of: link)
attributedString.addAttribute(.link, value: url, range: range)

let label = UILabel()
label.attributedText = attributedString
```

To make your app more accessible, you can also set the [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits) as [`.link`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620178-link):
```swift
label.accessibilityTraits = .link
```
