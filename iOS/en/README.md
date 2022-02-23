# Accessibility code examples for iOS apps

This folder contains accessibility code examples for iOS apps. Each success criterion has it's own file. This README file contains an overview of the most important techniques.

Visit [appt.org](https://appt.org/) for additional app accessibility knowledge.

## Table of Contents <!-- omit in toc -->

- [1. Set accessibility label](#1-set-accessibility-label)
- [2. Set accessibility focus](#2-set-accessibility-focus)
- [3. Set accessibility visibility](#3-set-accessibility-visibility)
- [4. Mark accessibility button](#4-mark-accessibility-button)
- [5. Mark accessibility header](#5-mark-accessibility-header)
- [6. Add accessibility description](#6-add-accessibility-description)
- [7. Group accessibility elements](#7-group-accessibility-elements)
- [8. Set accessibility order](#8-set-accessibility-order)
- [9. UIFont accessibility](#9-uifont-accessibility)
- [10. UIButton accessibility](#10-uibutton-accessibility)
  - [10.1. Allow multiple lines](#101-allow-multiple-lines)
  - [10.2. Allow larger width](#102-allow-larger-width)
- [11. NSAttributedString accessibility](#11-nsattributedstring-accessibility)
  - [11.1. Split into paragraphs](#111-split-into-paragraphs)
  - [11.2. Determine attribute values](#112-determine-attribute-values)
    - [Finding attributes](#finding-attributes)
    - [Detecting paragraph style](#detecting-paragraph-style)
    - [Detecting header style](#detecting-header-style)
    - [Detecting list items](#detecting-list-items)
    - [Detecting empty paragraphs](#detecting-empty-paragraphs)
    - [Calculating line height](#calculating-line-height)
  - [11.3. Create interface elements](#113-create-interface-elements)
- [Acknowledgements](#acknowledgements)

## 1. Set accessibility label

You can set a custom label which assistive technologies use by setting the `accessibilityLabel` property.

```swift
func label(_ view: UIView, label: String) -> UIView {
    view.accessibilityLabel = label
    return view
}
```

## 2. Set accessibility focus

Sometimes you want to move the accessibility focus to a specific view. You can do so by sending a `layoutChanged` accessibility notification and pass the specific view.

```swift
func focus(_ view: UIView) {
    UIAccessibility.post(notification: .layoutChanged, argument: view)
}
```

## 3. Set accessibility visibility

Certain views are not important for assistive technologies, such as decorative images. You can hide a view for assistive technologies using the `isAccessibilityElement` property.

```swift
func visible(_ view: UIView, visible: Boolean) -> UIView {
    view.isAccessibilityElement = visible
    return view
}
```

## 4. Mark accessibility button

You can mark a view as accessibility button by including the `button` trait in the `accessibilityTraits` property.

```swift
func button(_ view: UIView) -> UIView {
    view.accessibilityTraits = .button
}
```

## 5. Mark accessibility header

You can mark a view as accessibility header by including the `header` trait in the `accessibilityTraits` property.

```swift
func header(_ view: UIView) -> UIView {
    view.accessibilityTraits = .header
    return view
}
```

## 6. Add accessibility description

When interactive elements behave differently than a user might expect, you can add an accessibility description. You can describe the action which will happen on activation by using the `accesibilityHint` property.

```swift
func description(_ view: UIView, description: String) -> UIView {
    view.accessibilityHint = description
    return view
}
```

## 7. Group accessibility elements

In lists and other places, it often makes sense to group multiple elements together for users of assistive technologies. For example, let's say you have a list with items containing a date and title. You can group the date and title together by setting the `shouldGroupAccessibilityChildren`, `isAccessibilityElement` and `accessibilityLabel` properties on the root view:

```swift
func group(_ view: UIView, label: String) -> UIView {
    view.shouldGroupAccessibilityChildren = true
    view.isAccessibilityElement = true
    view.accessibilityLabel = label
    return view
}
```

## 8. Set accessibility order

The accessibility order usually matches the visual order. But sometimes a different accessibility order makes more sense. For example, let's say you have a list of items and an action button below it. It's not ideal if users have to navigate through all of the list items before they reach the action button. The `accessibilityElements` property can be used to change the order.

```swift
func order(_ view: UIView, _ elements: [Any]) {
    view.accessibilityElements = elements
    return view
}
```

## 9. UIFont accessibility

When using a custom font, you need to take [Dynamic Type](https://developer.apple.com/documentation/uikit/uifont/scaling_fonts_automatically) into account. If you don't, fonts are smaller or larger than the user prefers. You can use `UIFontMetrics` to scale the font to the size the user prefers.

```swift
extension UIFont {
    static func font(name: String, size: CGFloat, style: TextStyle) -> UIFont {
        guard let font = UIFont(name: name, size: size) else {
            fatalError("Font \(name) does not exist")
        }
        return UIFontMetrics(forTextStyle: style).scaledFont(for: font)
    }
}
```

You can also take it a step further by taking the `UIAccessibility.isBoldTextEnabled` property into account. Some users prefer to have all text displayed with a bold font.

## 10. UIButton accessibility

By default, the UIButton is not accessible as you might expect. You need to subclass it to pass the WCAG requirements.

**Update:** UIBUtton has support for multiple lines since iOS 15.

### 10.1. Allow multiple lines

One of the requirements from [WCAG 1.4.10](https://www.w3.org/WAI/WCAG21/Understanding/reflow.html) is that content should not be cut off when enlarged. By default, the text displayed by a `UIButton` is single line and truncated if it exceeds the maximum width.

During initialization, set `numberOfLines` to 0 to allow multiples lines. Set `lineBreakMode` to `.byWordWrapping` to break lines on words.

```swift
self.titleLabel?.lineBreakMode = .byWordWrapping
self.titleLabel?.numberOfLines = 0
```

The `preferredMaxLayoutWidth` of the button needs to be based on the frame size of the `titleLabel`.

```swift
override func layoutSubviews() {
    super.layoutSubviews()
    titleLabel?.preferredMaxLayoutWidth = titleLabel?.frame.size.width ?? 0
}
```

Full example here: [Button.swift](https://github.com/minvws/nl-covid19-coronacheck-app-ios/blob/main/Sources/CTR/Interface/Common/Button.swift)

### 10.2. Allow larger width

When users have increased their font size setting, a button can grow larger in width than expected.
Try to avoid fixed widths like `equalToConstant`. Instead, use a `greaterThanOrEqualToConstant` to allow larger widths when needed.
For most users, the buttons will have an equal width, but for those with larger font size, they can grow in width for better readability.

```swift
primaryButton.widthAnchor.constraint(
    greaterThanOrEqualToConstant: ViewTraits.buttonWidth),
    primaryButton.leadingAnchor.constraint(
        greaterThanOrEqualTo: safeAreaLayoutGuide.leadingAnchor,
        constant: ViewTraits.buttonMargin
    )
)
```

The `intrinsicContentSize` of the button needs to be calculated based on the `intrinsicContentSize` of the `titleLabel`.

```swift
/// Calculates content size including insets for dynamic font size scaling
override var intrinsicContentSize: CGSize {
    let fittingSize = titleLabel?.sizeThatFits(
        CGSize(width: frame.width, height: .greatestFiniteMagnitude)
    ) ?? .zero
    let intrinsicSize = titleLabel?.intrinsicContentSize ?? CGSize.zero

    let maxWidth = max(fittingSize.width, intrinsicSize.width)
    let maxHeight = max(fittingSize.height, intrinsicSize.height)

    let horizontalContentPadding = contentEdgeInsets.left + contentEdgeInsets.right
    let verticalContentPadding = contentEdgeInsets.top + contentEdgeInsets.bottom

    let horizontalImagePadding = abs(imageEdgeInsets.left) + abs(imageEdgeInsets.right)
    let verticalImagePadding = imageEdgeInsets.top + imageEdgeInsets.bottom

    let verticalPadding = max(verticalContentPadding, verticalImagePadding)

    return CGSize(
        width: maxWidth + horizontalContentPadding + horizontalImagePadding,
        height: maxHeight + verticalPadding
    )
}
```

Check out the full source code: [Button.swift](https://github.com/minvws/nl-covid19-coronacheck-app-ios/blob/main/Sources/CTR/Interface/Common/Button.swift)

## 11. NSAttributedString accessibility

It is often a requirement to markup text in a specific way. It can be tempting to write and parse HTML to achieve this. For example:

```html
Sentence with <strong>bold</strong> emphasis.

<h1>Important list</h1>
<ul>
    <li>List item 1</li>
    <li>List item 2</li>
</ul>
```

You can initialize a `NSAttributedString` with the HTML to create a String with the desired formatting.

**But there is a big accessibility problem: the markup is lost during the conversion.** The result is that the screen reader announces all text at once. One of the requirements from [WCAG 1.3.1](https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships.html) is that assistive technologies should be able to access the information and relationships that are displayed visually.

This means that users need to be able to navigate the list items one by one, and the "Important list" heading should be marked up as heading.

To achieve this, each paragraph needs to consist of its own interface element. My recommendation is to populate a `UITableView` or `UIStackView` and avoid using HTML. But if this is not a viable option, you can follow three steps to improve the accessibility.

### 11.1. Split into paragraphs

By splitting text on the linebreak (`\n`) character you can create an array of paragraphs. First, use the `components` method to split, then use the `attributedSubstring` method to create an array of `NSAttributedString`.

```swift
extension NSAttributedString {
    /// Helper method to split an attributed string by using the given separator
    func split(_ separator: String) -> [NSAttributedString] {
        var substrings = [NSAttributedString]()

        var index = 0
        for component in self.string.components(separatedBy: separator) {
            let range = NSRange(location: index, length: component.utf16.count)

            let substring = self.attributedSubstring(from: range)
            substrings.append(substring)

            index += range.length + separator.count
        }

        return substrings
    }
}
```

### 11.2. Determine attribute values

We now have an array of `NSAttributedString`, each representing a paragraph of text. To create the correct markup, it's important to detect headers, list items and empty paragraphs.

#### Finding attributes

We can determine the type based on the attributes that are set. We created a helper extension to check if a certain attribute is set:

```swift
extension NSAttributedString {
    /// Helper method to find certain attributes of an attributed string
    func attributes(find: (_ key: Key, _ value: Any, _ range: NSRange) -> (Bool)) -> Bool {
        var result = false
        enumerateAttributes(in: NSRange(location: 0, length: self.length)) { attributes, range, stop in
            for (key, value) in attributes {
                if find(key, value, range) {
                    result = true
                    break
                }
            }
        }
        return result
    }
}
```

#### Detecting paragraph style

Some of the attribute data required is stored inside `NSParagraphStyle`. For some reason, the [headerLevel](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1535869-headerlevel) and [textLists](https://developer.apple.com/documentation/appkit/nsparagraphstyle/1534193-textlists) attributes are available on macOS, but not on iOS. When debugging the object, it turns out the data is also set on iOS and can be accessed through key value access.

```swift
extension NSParagraphStyle {

    var headerLevel: Int {
        let key = "headerLevel"
        if responds(to: NSSelectorFromString(key)) {
            return value(forKey: key) as? Int ?? 0
        }
        return 0
    }

    var textLists: NSArray {
        let key = "textLists"
        if responds(to: NSSelectorFromString(key)) {
            return value(forKey: key) as? NSArray ?? []
        }
        return []
    }
}
```

#### Detecting header style

When a paragraph uses a `<h1>`-`<h6>` tag, it is a header. You can also mark a paragraph as header when all characters use a bold font.

```swift
extension NSAttributedString {
    /// Determines whether the attributed string is a header
    var isHeader: Bool {
        return attributes { key, value, range in
            // Check if header level is h1 or higher
            if key == NSAttributedString.Key.paragraphStyle,
               let paragraphStyle = value as? NSParagraphStyle,
               paragraphStyle.headerLevel >= 1 {
                return true
            }

            // Check if full range uses a bold font
            if key == NSAttributedString.Key.font,
               let font = value as? UIFont,
               font.fontDescriptor.symbolicTraits.contains(.traitBold),
               range.lowerBound == 0,
               range.upperBound >= self.length - 1 {
                return true
            }

            return false
        }
    }
}
```

#### Detecting list items

If the textLists property contains one or more items, it is a list item. Depending on your parsing strategy, a list item could also start with a (tabbed) bullet character.

```swift
extension NSAttributedString {
    /// Determines whether the attributed string is a list item
    var isListItem: Bool {
        // Check if strings starts with tabbed bullet character
        if string.starts(with: "\t●") || string.starts(with: "\t•") {
            return true
        }

        // Check if textLists attribute contains one or more elements
        return attributes { key, value, _ in
            if key == NSAttributedString.Key.paragraphStyle,
               let paragraphStyle = value as? NSParagraphStyle,
               paragraphStyle.textLists.count > 0 {
                return true
            }
            return false
        }
    }
}
```

#### Detecting empty paragraphs

If a paragraph only contains whitespace characters, it should be ignored by assistive technologies. Whitespace can be detected this way:

```swift
extension NSAttributedString {
    /// Determines if the attributed string is blank
    var isBlank: Bool {
        return string.trimmingCharacters(in: .whitespaces).isEmpty
    }
}
```

#### Calculating line height

There must be spacing between each paragraph. The maximum value of the `minimumLineHeight` property can be used as spacing.

```swift
extension NSAttributedString {
    /// Determines the line height used for the attributed string
    var lineHeight: CGFloat {
        var height: CGFloat = 0

        // Retrieve the maximum value set for minimumLineHeight in NSParagraphStyle
        enumerateAttributes(in: NSRange(location: 0, length: self.length)) { attributes, range, stop in
            for (key, value) in attributes {
                if key == NSAttributedString.Key.paragraphStyle,
                    let paragraphStyle = value as? NSParagraphStyle,
                    paragraphStyle.minimumLineHeight > height {
                    height = paragraphStyle.minimumLineHeight
                }
            }
        }

        return height
    }
}
```

### 11.3. Create interface elements

Now that we have our paragraphs and are able to determine the attributes, it's time to create interface elements.

Create a subclass of `UIStackView` named `TextView`. Add the `attributedText` property, to replicate the `attributedText` property `UITextView`.

Create a subclass of `UITextView` named `TextElement`. Each TextElement will display one paragraph of text. The most basic implementation only sets the `attributedText` property.

Putting everything together:

```swift
class TextView: UIStackView {

    var paragraphMarginMultiplier: CGFloat = 1.0
    var headerMarginMultiplier: CGFloat = 0.25
    var listItemMarginMultiplier: CGFloat = 0.25

    /// Helper variable to display a TextElement for each paragraph in the attributed string
    var attributedText: NSAttributedString? {
        didSet {
            removeAllArrangedSubviews()

            guard let attributedText = attributedText else { return }

            // Split attributed text on new line
            let parts = attributedText.split("\n")

            for part in parts {
                // 1. Determine spacing of previous element
                if let previousElement = arrangedSubviews.last {
                    var spacing = part.lineHeight

                    if part.isHeader {
                        spacing *= headerMarginMultiplier
                    } else if part.isListItem {
                        spacing *= listItemMarginMultiplier
                    } else {
                        spacing *= paragraphMarginMultiplier
                    }

                    setCustomSpacing(spacing, after: previousElement)
                }

                // 2. Add current TextElement
                let element = TextElement(attributedText: part)

                // Mark as header?
                if part.isHeader {
                    element.accessibilityTraits = .header
                }

                // Hide for assistive technologies?
                if part.isBlank {
                    element.isAccessibilityElement = false
                }

                addArrangedSubview(element)
            }
        }
    }
}
```

Depending on your styling requirements, you might need some more tweaks to make everything appear correctly.

Check out the full code here: [TextView.swift](https://github.com/minvws/nl-covid19-coronacheck-app-ios/blob/main/Sources/CTR/Interface/Common/TextView.swift]) and [TextElement.swift](https://github.com/minvws/nl-covid19-coronacheck-app-ios/blob/main/Sources/CTR/Interface/Common/TextElement.swift).

## Acknowledgements

These code examples are based on:

- [appt-ios](https://github.com/appt-nl/appt-ios), licensed under [MIT](https://opensource.org/licenses/MIT)
- [nl-covid19-coronacheck-app-ios](https://github.com/minvws/nl-covid19-coronacheck-app-ios/commits?author=JJdeGroot), licensed under [EUPL-1.2](https://opensource.org/licenses/EUPL-1.2)
- [nl-covid19-dbco-app-ios](https://github.com/minvws/nl-covid19-dbco-app-ios/commits?author=JJdeGroot), licensed under [EUPL-1.2](https://opensource.org/licenses/EUPL-1.2)
- [nl-covid19-notification-app-ios](https://github.com/minvws/nl-covid19-notification-app-ios/commits?author=JJdeGroot), licensed under [EUPL-1.2](https://opensource.org/licenses/EUPL-1.2)