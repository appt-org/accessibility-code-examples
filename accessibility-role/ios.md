On iOS, the [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits) attribute is used to indicate an accessibility role. The [`UIAccessibilityTraits`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits) structure contains all options, such as [`header`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620170-header), [`button`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620194-button), [`link`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620178-link) and [`image`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620174-image), among others.

```swift
element.accessibilityTraits = .button
element.accessibilityTraits = .header
element.accessibilityTraits = .link
element.accessibilityTraits = .image
```
