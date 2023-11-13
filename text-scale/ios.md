# Scale text - iOS

On iOS, you can use [Dynamic Font Size](https://developer.apple.com/documentation/uikit/uifont/scaling_fonts_automatically) to scale text. By using this function, the font size is adjusted to the preferences of the user. If you're using your own font, you can use the [`scaledFont`](https://developer.apple.com/documentation/uikit/uifontmetrics/2877385-scaledfont) method from [`UIFontMetrics`](https://developer.apple.com/documentation/uikit/uifontmetrics) to calculate the font size.

Text elements such as `UILabel`, `UITextField` and `UITextView` have a property called [`adjustsFontForContentSizeCategory`](https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting/1771731-adjustsfontforcontentsizecategor). If you set it to `true`,  the element automatically updates its font when the device's content size category changes.

For `adjustsFontForContentSizeCategory` to take effect, the element’s font must be one of the following:
- A font vended using [`preferredFont(forTextStyle:)`](https://developer.apple.com/documentation/uikit/uifont/1619030-preferredfont) or [`preferredFont(forTextStyle:compatibleWith:)`](https://developer.apple.com/documentation/uikit/uifont/1771762-preferredfont) with a valid [`UIFont.TextStyle`](https://developer.apple.com/documentation/uikit/uifont/textstyle)
- A font vended using [`UIFontMetrics.scaledFont(for:)`](https://developer.apple.com/documentation/uikit/uifontmetrics/2877385-scaledfont) or one of its variants

```swift
// MARK: - Scaling custom fonts
import UIKit

extension UIFont {

    static func font(name: String, size: CGFloat, style: TextStyle) -> UIFont {
        guard let font = UIFont(name: name, size: size) else {
            fatalError("Font \(name) does not exist")
        }
        return UIFontMetrics(forTextStyle: style).scaledFont(for: font)
    }
    
    static func openSans(weight: UIFont.Weight, size: CGFloat, style: TextStyle) -> UIFont {
        if UIAccessibility.isBoldTextEnabled {
            return font(name: "OpenSans-Bold", size: size, style: style)
        }
        
        switch weight {
            case .regular:
                return font(name: "OpenSans-Regular", size: size, style: style)
            case .semibold:
                return font(name: "OpenSans-SemiBold", size: size, style: style)
            case .bold:
                return font(name: "OpenSans-Bold", size: size, style: style)
            default:
                fatalError("Font weight \(weight) is not supported")
        }
    }
}

// MARK: - Enabling content size category adjustments
label.adjustsFontForContentSizeCategory = true
```
