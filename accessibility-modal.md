# Accessibility modal

A modal overlays the screen with additional content. Modals are usually indicated visually, e.g. by throwing a shadow on the content below it. Users of assistive technologies also need to know when content is part of a modal.

## WCAG

Relates to 1.3.1

## Android

On Android, there is no method to indicate an accessibility modal. However, you can can indicate an accessibility pane by using the [`setPaneTitle`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setPaneTitle(java.lang.CharSequence)) method. `ViewCompat` also contains a convenience method: [`setAccessibilityPaneTitle`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityPaneTitle(android.view.View,java.lang.CharSequence)). Please keep in mind that is focus is not trapped when a pane title has been set.

```kotlin
ViewCompat.setAccessibilityPaneTitle(view, "Appt pane")
```

## iOS

On iOS, you can indicate an accessibility modal by using the  [`accessibilityViewIsModal`](https://developer.apple.com/documentation/objectivec/nsobject/1615089-accessibilityviewismodal) property.

```swift
viewController.accessibilityViewIsModal = true
```

## Flutter

On Flutter, the [`ModelBarrier`](https://api.flutter.dev/flutter/widgets/ModalBarrier-class.html) class takes accessibility into account. The [`barrierDismissable`](https://api.flutter.dev/flutter/widgets/ModalRoute/barrierDismissible.html) and [`barrierLabel`](https://api.flutter.dev/flutter/widgets/ModalRoute/barrierLabel.html) are used by assistive technologies. When `barrierDismissable` is set to false, the focus of assistive technologies is trapped inside the modal. The value of  `barrierLabel` is announced upon entering the modal.

```dart
showDialog(
    context: context,
    barrierDismissible: false,
    barrierLabel: 'Label'
    builder: (context) {
        return SimpleDialog(
            title: Text('Appt')
        );
    },
);
```

## React Native

With React Native, you can use the [`accessibilityViewIsModal`](https://reactnative.dev/docs/accessibility#accessibilityviewismodal-ios) prop to mark an accessibility modal. This prop only works on iOS.

```jsx
<Modal accessibilityViewIsModal={true}>
    <Text>Appt</Text>
</Modal>
```

## Xamarin

Xamarin Forms does not have built-in support to indicate an accessibility modal.

```xml
Not available, contribute!
```
