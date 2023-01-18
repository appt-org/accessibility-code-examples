# Keyboard shortcuts

Most people operate their smartphones with touch, but some people use an external keyboard. Learning and using keyboard shortcuts can save you a lot of time. Shortcuts should always use a modifier key, such as `CTRL` or `CMD` to avoid clashing with system shortcuts.

## WCAG

Relates to 2.1.4

## Android

On Android, you can use the [`dispatchKeyEvent`](https://developer.android.com/reference/android/view/View#dispatchKeyEvent(android.view.KeyEvent)) and [`onKeyUp`](https://developer.android.com/reference/android/app/Activity#onKeyUp(int,%20android.view.KeyEvent)) methods to activate shortcuts. Both methods give you a reference to a [`KeyEvent`](https://developer.android.com/reference/android/view/KeyEvent) object. Use the [`isShiftPressed`](https://developer.android.com/reference/android/view/KeyEvent#isShiftPressed()) or [`isCtrlPressed`](https://developer.android.com/reference/android/view/KeyEvent#isCtrlPressed()) method to make sure that shortcuts are not activated by accident.

```kotlin
override fun onKeyUp(keyCode: Int, event: KeyEvent): Boolean {
    return when (keyCode) {
        KeyEvent.KEYCODE_F -> {
            if (event.isCtrlPressed) {
                find()
                true
            }
        }
        else -> super.onKeyUp(keyCode, event)
    }
}

private fun find() {
    // Logic
}
```

## iOS

On iOS, the [`pressesBegan`](https://developer.apple.com/documentation/uikit/uiresponder/1621134-pressesbegan) and [`pressesEnded`](https://developer.apple.com/documentation/uikit/uiresponder/1621128-pressesended) can be used to activate shortcuts. But, you should use [`UIKeyCommand`](https://developer.apple.com/documentation/uikit/uikeycommand) to add keyboard shortcuts. By adding [`modifierFlags`](https://developer.apple.com/documentation/uikit/uikeymodifierflags) you can be sure that shortcuts are not activated by accident. An additional advantage is that `UIKeyCommand`-shortcuts are shown when long pressing the command key.

```swift
let find = UIKeyCommand(
    input: "f", 
    modifierFlags: .command, 
    action: #selector(findContent), 
    discoverabilityTitle: "Find"
)

override var keyCommands: [UIKeyCommand]? {
    return [find]
}

@objc private func find() {
    // Logic
}
```

## Flutter

With Flutter, you can use the [`RawKeyboard`](https://api.flutter.dev/flutter/services/RawKeyboard-class.html) listener to implement shortcuts in your app. The `RawKeyboard` listener yields a [`RawKeyUpEvent`](https://api.flutter.dev/flutter/services/RawKeyUpEvent-class.html) of a [`RawKeyDownEvent`](https://api.flutter.dev/flutter/services/RawKeyDownEvent-class.html). The `data` attribute has a `isModifierPressed()` method that can be used to determine whether a modifier key has been pressed.

```dart
RawKeyboard.instance.addListener((keyEvent) {
  if (keyEvent is RawKeyUpEvent) {
    if (keyEvent.logicalKey == LogicalKeyboardKey.keyF &&
        keyEvent.data.isModifierPressed(ModifierKey.controlModifier)) {
      find();
    }
  }
});

void find() {
    // Logic
}
```

## React Native

React Native does not support binding custom key events for shortcuts. The package [`react-native-keyevent`](https://github.com/kevinejohn/react-native-keyevent) allows you to capture external keyboard keys. However, it [only works on Android](https://github.com/kevinejohn/react-native-keyevent).

```jsx
componentDidMount() {
    KeyEvent.onKeyMultipleListener((keyEvent) => {
        console.log(`onKeyMultiple keyCode: ${keyEvent.keyCode}`);
        console.log(`Action: ${keyEvent.action}`);
        console.log(`Characters: ${keyEvent.characters}`);
    });
}

componentWillUnmount() {
    KeyEvent.removeKeyMultipleListener();
}
```

## Xamarin

Xamarin does not have support for hardware keyboard events. However, you can intercept key events inside the Android and iOS application.

- Android: hook into [`onKeyUp`](https://learn.microsoft.com/en-us/dotnet/api/android.app.activity.onkeyup?view=xamarin-android-sdk-12) inside `MainActivity.cs`
- iOS: hook into [`KeyCommands`](https://learn.microsoft.com/en-us/dotnet/api/uikit.uiresponder.keycommands?view=xamarin-ios-sdk-12) using a [custom renderer](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/custom-renderer/contentpage).

The code example below shows a sample implementation for iOS.

```csharp
[assembly: ExportRenderer(typeof(ContentPage), typeof(KeyboardPageRenderer))]
namespace KeyCommandsInXamarinForms.iOS
{
    public class KeyboardPageRenderer : PageRenderer
    {
        protected override void OnElementChanged(VisualElementChangedEventArgs e)
        {
            base.OnElementChanged(e);

            if (e.OldElement != null || Element == null)
            {
                return;
            }

            // Create key command for Command + F
            UIKeyCommand command1 = UIKeyCommand.Create(
                new NSString("F"), 
                UIKeyModifierFlags.Command, 
                new ObjCRuntime.Selector("OnKeyPressed:")
            );

            this.AddKeyCommand(command1);
        }

        [Export("OnKeyPressed:")]
        private void Excute(UIKeyCommand keyCommand)
        {
            // Find
        }

        public override bool CanBecomeFirstResponder
        {
            get
            {
                return true; // Key commands require first responder
            }
        }
    }
}
```

The code example below shows a sample implementation for Android.

```csharp
public override bool OnKeyUp([GeneratedEnum] Keycode keyCode, KeyEvent e)
{
    if (keyCode == Keycode.KEYCODE_F && e.isCtrlPressed)
    {
        // Search
        return true
    }

    return base.OnKeyUp(keyCode, e);
}
```
