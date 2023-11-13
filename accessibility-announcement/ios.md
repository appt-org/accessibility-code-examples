# Accessibility announcement - iOS

On iOS, you post an accessibility message by using the [`UIAccessibility`](https://developer.apple.com/documentation/uikit/uiaccessibility) object. The [`post`](https://developer.apple.com/documentation/uikit/uiaccessibility/1615194-post) method can be used to post data to assistive technologies. Set the type to [`announcement`](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/1620176-announcement) and supply a `string` argument to announce something.

```swift
UIAccessibility.post(notification: .announcement, argument: "Appt announcement")
```
