On iOS, you can use [Dynamic Font Size](https://developer.apple.com/documentation/uikit/uifont/scaling_fonts_automatically) to scale text. By using this function, the font size is adjusted to the preferences of the user. If you're using your own font, you can use the [`scaledFont`](https://developer.apple.com/documentation/uikit/uifontmetrics/2877385-scaledfont) method from [`UIFontMetrics`](https://developer.apple.com/documentation/uikit/uifontmetrics) to calculate the font size.

```swift
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
```

`UILabel`, `UITextField` and `UITextView` have a property called [`adjustsFontForContentSizeCategory`](https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting/1771731-adjustsfontforcontentsizecategor). If you set it as `true`,  the component automatically updates its font when the device's content size category changes.

```swift
label.adjustsFontForContentSizeCategory = true
```
