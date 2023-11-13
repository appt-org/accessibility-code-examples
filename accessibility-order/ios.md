# Accessibility order - iOS

On iOS, you can use the [`accessibilityElements`](https://developer.apple.com/documentation/objectivec/nsobject/1615147-accessibilityelements) property to set the order for assistive technologies. Be careful using the `accessibilityElements` property, because any elements left out of the array cannot be reached with assistive technologies.

```swift
view.accessibilityElements = [header, description, list]
```
