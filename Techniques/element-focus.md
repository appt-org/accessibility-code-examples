# Element focus change

Whenever an element receives focus, it should not automatically trigger an event which changes `context`. Example of changing context include, but are not limited to: automatically submitting data, opening a new screen or moving to another element. Focus should only be moved deliberately by the user.

## Android

On Android, you can use an [`OnFocusChangeListener`](https://developer.android.com/reference/android/view/View.OnFocusChangeListener) to listen to focus changes. The [`onFocusChange`](https://developer.android.com/reference/android/view/View.OnFocusChangeListener#onFocusChange(android.view.View,%20boolean)) method is called when the element receives focus.

Be careful when using the `onFocusChange` method: don't trigger any context change because they might confuse users.

```kotlin
webView.setOnFocusChangeListener { view, focused ->
    if (focused) {
        // Don't trigger context changes
    }
}
```

## iOS

On iOS, you can use the [`UIAccessibilityFocus`](https://developer.apple.com/documentation/objectivec/nsobject/uiaccessibilityfocus) protocol to listen to focus changes. The [`accessibilityElementDidBecomeFocused`](https://developer.apple.com/documentation/objectivec/nsobject/1615183-accessibilityelementdidbecomefoc) method is called whenever an element receives focus.

Be careful when using the `accessibilityElementDidBecomeFocused` method: don't trigger any context change because they might confuse users.

```swift
class View: UIView {
    
    override open func accessibilityElementDidBecomeFocused() {
        // Don't trigger context changes
    }
}
```

## Flutter

In Flutter, you can use [`FocusNode`](https://api.flutter.dev/flutter/widgets/FocusNode-class.html) to listen to focus changes. The [`flutter_hooks`](https://pub.dev/packages/flutter_hooks) package includes a method named [`useFocusNode`](https://pub.dev/documentation/flutter_hooks/latest/flutter_hooks/useFocusNode.html) which makes it easier to listen to to focus changes.

Be careful when using the `FocusNode` listener: don't trigger any context change because they might confuse users.

```dart
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';

class FocusWidget extends HookWidget {
    @override
    Widget build(BuildContext context) {
        final focusNode = useFocusNode();
        useEffect(() {
            focusNode.addListener(() {
                // Don't trigger context changes
            });
            return;
        }, [focusNode]);

        return TextField(focusNode: focusNode);
    }
}
```

## React Native

In React Native, you can use the [`onFocus`](https://reactnative.dev/docs/next/textinput#onfocus) method to listen to focus changes. The method is called when the element receives focus.

Be careful when the `onFocus` callback: don't trigger any context change because they might confuse users.

```jsx
<TextInput onFocus={() => {
    // Don't trigger context changes
}} />
```

## Xamarin

In Xamarin.Forms, you can use the [`Focused`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.visualelement.focused?view=xamarin-forms) event to listen to focus changes. The method is called when the element receives focus.

Be careful when the `Focused` callback: don't trigger any context change because they might confuse users.

```csharp
Element.Focused += (sender, arguments) => {
    // Don't trigger context changes
};
```
