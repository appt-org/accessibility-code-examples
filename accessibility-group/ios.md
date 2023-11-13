# Accessibility group - iOS

On iOS, you can group elements by setting [`isAccessibilityElement`](https://developer.apple.com/documentation/objectivec/nsobject/1615141-isaccessibilityelement) to `true` on the parent element. Don't forget to set an [`accessibilityLabel`](https://developer.apple.com/documentation/objectivec/nsobject/1615181-accessibilitylabel) for the group.

Sometimes it can be useful to also the [`shouldGroupAccessibilityChildren`](https://developer.apple.com/documentation/objectivec/nsobject/1615143-shouldgroupaccessibilitychildren) property to group the accessibility elements that are children of the element, regardless of their positions on the screen.

```swift
group.isAccessibilityElement = true
group.shouldGroupAccessibilityChildren = true
group.accessibilityLabel = "Appt group"
```
