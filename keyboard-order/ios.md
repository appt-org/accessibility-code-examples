# Keyboard order - iOS

On iOS, you can use the [`accessibilityRespondsToUserInteraction`](https://developer.apple.com/documentation/objectivec/nsobject/3043551-accessibilityrespondstouserinter) attribute to optimize keyboard navigation. By setting the property to `false`, the element will be skipped with keyboard navigation. Other assistive technologies, such as VoiceOver can still focus on the element. This way you can provide screen reader users with alternative text for images, but skip focus for keyboard users. When a hardware keyboard is connected and VoiceOver is enabled, the image will be focusable.

For even more concise control over the keyboard order, you can use properties such as [`canBecomeFocused`](https://developer.apple.com/documentation/uikit/uiview/1622584-canbecomefocused),[`focusGroupIdentifier`](https://developer.apple.com/documentation/uikit/uiview/3601233-focusgroupidentifier) and [`focusGroupPriority`](https://developer.apple.com/documentation/uikit/uiview/3778579-focusgrouppriority).
To debug focus, you can use [`UIFocusDebugger`](https://developer.apple.com/documentation/uikit/uifocusdebugger).

A use case could be a grid where you want to navigate by rows. You can achieve this by setting the same `focusGroupIdentifier` for each column in a row.

```swift
grid.topLeft.focusGroupIdentifier = "top"
grid.topRight.focusGroupIdentifier = "top"
grid.bottomLeft.focusGroupIdentifier = "bottom"
grid.bottomRight.focusGroupIdentifier = "bottom"
```
