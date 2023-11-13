# Accessibility live region - iOS

On iOS, the closest thing to live regions are elements with the [`updatesFrequently`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620187-updatesfrequently) trait. When an element is focused, label and value changes are announced periodically.

You can replicate a live region by posting accessibility announcements. To replicate 'polite' behavior, you can set [`accessibilitySpeechQueueAnnouncement`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/2865770-accessibilityspeechqueueannounce) to `false`. To be 'asssertive', set the value to `true`.

For even more advanced behavior, you can use act on [`announcementDidFinishNotification`](https://developer.apple.com/documentation/uikit/uiaccessibility/1620202-announcementdidfinishnotificatio) events.

```swift
// Periodic announcements (only on focus!)
element.accessibilityTraits = .updatesFrequently

// Replicate live region
let message = NSAttributedString(
    string: "Appt live region", 
    attributes: [.accessibilitySpeechQueueAnnouncement: true]
)
UIAccessibility.post(notification: .announcement, argument: message)
```
