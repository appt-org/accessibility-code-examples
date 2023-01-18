# Accessibility focus

Sometimes you need to programmatically move the accessibility focus to a specific element. For example, when you present a modal, the assistive technology should move it's focus to it. Or when moving to a new screen, you might want assistive technologies to focus a specific element.

## WCAG

Relates to 2.1.1, 2.4.3

## Android

On Android, you can send an [`AccessibilityEvent`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent) of the type [`TYPE_VIEW_FOCUSED`](https://developer.android.com/reference/android/view/accessibility/AccessibilityEvent#TYPE_VIEW_FOCUSED) to move the focus of assistive technologies to a specific view. The view must be focusable for this event to take effect.

```kotlin
fun focus(view: View) {
    view.sendAccessibilityEvent(AccessibilityEvent.TYPE_VIEW_FOCUSED)
}
```

## iOS

On iOS, you can use [`UIAccessibility`](https://developer.apple.com/documentation/objectivec/nsobject/uiaccessibility) to [`post`](https://developer.apple.com/documentation/uikit/uiaccessibility/1615194-post) a notification to move the focus of assistive technologies. Use [`screenChanged`](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/1620198-screenchanged/) when a new view appears that occupies a major portion of the screen. Otherwise, use [`layoutChanged`](https://developer.apple.com/documentation/uikit/uiaccessibility/notification/1620186-layoutchanged) when the layout of current screen changes.

```swift
func focus(_ view: UIView) {
    UIAccessibility.post(notification: .layoutChanged, argument: view)
    UIAccessibility.post(notification: .screenChanged, argument: view)
}
```

## Flutter

Flutter does not have built-in support for changing accessibility focus. See [Flutter issue #59594](https://github.com/flutter/flutter/issues/59594) for more information.

You could implement your own [`platform channels`](https://docs.flutter.dev/development/platform-integration/platform-channels) to call the native Android and iOS methods to move accessibility focus.

Do not use `FocusNode` or `Semantics.focused`, these methods should only be used for keyboard or input focus.

```dart
Not available, contribute!
```

## React Native

In React Native you can move accessibility focus by using the [`setAccessibilityFocus`](https://reactnative.dev/docs/accessibilityinfo#setaccessibilityfocus) method from the [`AccessibilityInfo class`](https://reactnative.dev/docs/accessibilityinfo). This method requires a `reactTag`, which you can find by calling the `findNodeHandle` method.

```tsx
function Component() {
  const ref = useRef(null);
  
  function setFocus() {
    const reactTag = findNodeHandle(ref.current);
    
    if (reactTag) {
      AccessibilityInfo.setAccessibilityFocus(reactTag);
    }
  }

  return <View ref={ref} accessible accessibilityLabel="Modal" />
};
```

## Xamarin

Xamarin Forms does not have built-in support for changing accessibility focus.

The [`SemanticExtensions`](https://github.com/xamarin/XamarinCommunityToolkit/blob/main/src/CommunityToolkit/Xamarin.CommunityToolkit/Extensions/Semantic/SemanticExtensions.shared.cs) file inside the [`Xamarin.CommunityToolkit`](https://github.com/xamarin/XamarinCommunityToolkit) contains the `SetSemanticFocus` method. It moves the accessibility focus to the given element on the native platform.

```csharp
SemanticExtensions.SetSemanticFocus(element)
```
