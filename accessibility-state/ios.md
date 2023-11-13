# Accessibility state - iOS

On iOS, the [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits) attribute can be used to indicate the accessibility state. The traits  [`selected`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620197-selected) and [`notEnabled`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620208-notenabled) can be used to indicate the current state.

If your state is not `selected` or `notEnabled`, we recommended using the [`accessibilityValue`](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619583-accessibilityvalue) attribute to indicate the state.

```swift
element.accessibilityTraits = .selected
element.accessibilityTraits = .notEnabled

element.accessibilityValue = "Expanded"
element.accessibilityValue = "Collapsed"
```
