# Text spacing - iOS

On iOS, you can use [`NSMutableParagraphStyle`](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle) for paragraphs:

- [`lineSpacing`](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1528742-linespacing): set spacing between lines
- [`lineHeightMultiple`](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1524596-lineheightmultiple): multiply distance between lines by a number
- [`paragraphSpacing`](https://developer.apple.com/documentation/uikit/nsmutableparagraphstyle/1532528-paragraphspacing): set spacing between paragraphs

To adjust the spacing between letters you can use the [`NSKernAttributeName`](https://developer.apple.com/documentation/uikit/nskernattributename) attribute.

```swift
let style = NSMutableParagraphStyle()
style.lineSpacing = 20
style.lineHeightMultiple = 1.5
style.paragraphSpacing = 20

let attributedString = NSAttributedString(string: "Appt", attributes: [
    .paragraphStyle:  style,
    .kern: 3.0
])
element.attributedText = attributedString
```
