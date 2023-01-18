# Element focus change

Whenever an element receives focus, it should not automatically trigger an event which changes `context`. Example of changing context include, but are not limited to: automatically submitting data, opening a new screen or moving to another element. Focus should only be moved deliberately by the user.

## WCAG

Relates to 3.2.1

## Android

On Android, you can use an [`OnFocusChangeListener`](https://developer.android.com/reference/android/view/View.OnFocusChangeListener) to listen to focus changes. The [`onFocusChange`](https://developer.android.com/reference/android/view/View.OnFocusChangeListener#onFocusChange(android.view.View,%20boolean)) method is called when the element receives focus.

Be careful when using the `onFocusChange` method: do not trigger any context change because they might confuse users.

```kotlin
webView.setOnFocusChangeListener { view, focused ->
    if (focused) {
        // Do not change context
    }
}
```

## iOS

On iOS, you can use the [`UIAccessibilityFocus`](https://developer.apple.com/documentation/objectivec/nsobject/uiaccessibilityfocus) protocol to listen to focus changes. The [`accessibilityElementDidBecomeFocused`](https://developer.apple.com/documentation/objectivec/nsobject/1615183-accessibilityelementdidbecomefoc) method is called whenever an element receives focus.

Be careful when using the `accessibilityElementDidBecomeFocused` method: do not trigger any context change because they might confuse users.

```swift
class View: UIView {
    
    override open func accessibilityElementDidBecomeFocused() {
        // Do not change context
    }
}
```

## Flutter

In Flutter, you can use [`FocusNode`](https://api.flutter.dev/flutter/widgets/FocusNode-class.html) to listen to focus changes. The [`flutter_hooks`](https://pub.dev/packages/flutter_hooks) package includes a method named [`useFocusNode`](https://pub.dev/documentation/flutter_hooks/latest/flutter_hooks/useFocusNode.html) which makes it easier to listen to to focus changes.

Be careful when using the `FocusNode` listener: do not trigger any context change because they might confuse users.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

class FocusWidget extends HookWidget {
    @override
    Widget build(BuildContext context) {
        final focusNode = useFocusNode();
        useEffect(() {
            focusNode.addListener(() {
                // Do not change context
            });
            return;
        }, [focusNode]);

        return TextField(focusNode: focusNode);
    }
}
```

## React Native

In React Native, you can use the [`onFocus`](https://reactnative.dev/docs/next/textinput#onfocus) method to listen to focus changes. The method is called when the element receives focus.

Be careful when the `onFocus` callback: do not trigger any context change because they might confuse users.

```jsx
<TextInput onFocus={() => {
    // Do not change context
}} />
```

## Xamarin

In Xamarin.Forms, you can use the [`Focused`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.visualelement.focused?view=xamarin-forms) event to listen to focus changes. The method is called when the element receives focus.

Be careful when the `Focused` callback: do not trigger any context change because they might confuse users.

```csharp
Element.Focused += (sender, arguments) => {
    // Do not change context
};
```
