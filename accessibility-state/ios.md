On iOS, the [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits) attribute can be used to indicate the accessibility state. The traits  [`selected`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620197-selected) and [`notEnabled`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620208-notenabled) can be used to indicate the current state.

Other values are listed in the  [`UIAccessibilityTraits`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits) structure.

```swift
element.accessibilityTraits = .selected
element.accessibilityTraits = .notEnabled
```
