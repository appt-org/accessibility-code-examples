# Accessibility role - iOS

On iOS, the [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits) attribute is used to indicate an accessibility role. The [`UIAccessibilityTraits`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits) structure contains all options, such as [`header`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620170-header), [`button`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620194-button), [`link`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620178-link) and [`image`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620174-image), among others.

You can also combine multiple traits. For example, for a selected button you can can pass both traits as an array: `[.button, .selected]`.

```swift
element.accessibilityTraits = .button
element.accessibilityTraits = .header
element.accessibilityTraits = .link
element.accessibilityTraits = .image

element.accessibilityTraits = [.button, .selected]
```
