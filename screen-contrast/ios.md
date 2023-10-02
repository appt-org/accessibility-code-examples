On iOS, can use [Xcode's Accessibility Inspector](https://developer.apple.com/library/archive/documentation/Accessibility/Conceptual/AccessibilityMacOSX/OSXAXTestingApps.html) to detect contrast issues automatically. You can also use the property [`accessibilityContrast`](https://developer.apple.com/documentation/uikit/uiaccessibilitycontrast) to check if the user set the contrast level in the Accessibility area in Settings.

```swift
if UITraitCollection.current.accessibilityContrast == .high {
    // code    
}
```
