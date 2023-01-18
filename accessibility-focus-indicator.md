# Accessibility focus indicator

Users should know which element has focus when using a keyboard or assistive technology. For example, you could show a rectangle around the focused element. Or you can adjust the colors whenever an element receives focus. Focus indicators can take many different forms. The focus indicator should remain visible while the element is in focused state.

## WCAG

Relates to 2.4.7

## Android

On Android, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings of Android.

You can use a [`ColorStateList`](https://developer.android.com/guide/topics/resources/color-list-resource) to change colors based on the element state. An element moves into the [`state_focused`](https://developer.android.com/reference/android/graphics/drawable/StateListDrawable#attr_android:state_focused) whenever it receives focus.

The code sample below shows how to change the background color of a button on focus.

```xml
<!-- selector.xml -->
<selector xmlns:android="http://schemas.android.com/apk/res/android">
    <item android:drawable="@color/focused" android:state_focused="true" />
    <item android:drawable="@color/default" />
</selector>

<!-- layout.xml -->
<Button
    android:id="@+id/button"
    android:background="@drawable/selector">
</Button>
```

## iOS

On iOS, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings of iOS.

You can override the [`accessibilityElementDidBecomeFocused`](https://developer.apple.com/documentation/objectivec/nsobject/1615183-accessibilityelementdidbecomefoc) and [`accessibilityElementDidLoseFocus`](https://developer.apple.com/documentation/objectivec/nsobject/1615082-accessibilityelementdidlosefocus) methods to listen to focus state changes. By subclassing an element, you can change the colors based on the element state.

The code sample below shows how to change the background color of a button on focus.

```swift
class Button: UIButton {
    
    override open func accessibilityElementDidBecomeFocused() {
        backgroundColor = .focused
    }

    override open func accessibilityElementDidLoseFocus() {
        backgrounColor = .default
    }
}
```

## Flutter

In Flutter, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings on Android and iOS.

You can change colors based on [`MaterialState`](https://api.flutter.dev/flutter/material/MaterialState.html). For a button, you could add a [`ButtonStyle`](https://api.flutter.dev/flutter/material/ButtonStyle-class.html) to change the color when in [`.focused`](https://api.flutter.dev/flutter/material/MaterialState.html#focused) state.

The code sample below shows how to change the background color of a button on focus.

```dart
TextButton(
  style: ButtonStyle(
    backgroundColor: MaterialStateProperty.resolveWith(getColor),
  ),
  child: Text('Button'),
);

Color? getColor(Set<MaterialState> states) {
  const Set<MaterialState> interactiveStates = <MaterialState>{
    MaterialState.focused,
  };
  if (states.any(interactiveStates.contains)) {
    return Colors.blue;
  }
  return Colors.red;
}
```

## React Native

In React Native, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings on Android and iOS.

```tsx
Not available, contribute!
```

## Xamarin

In Xamarin.Forms, you can adjust colors when an element receives focus. However, it's not possible to change the focus indicator of assistive technologies. Users can adjust their preferences in the system settings on Android and iOS.

The [`Visual State Manager`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/visual-state-manager) (VSM) provides a structured way to make visual changes to the user interface from code. The `VSM` contains a visual state group named `CommonStates` which includes the `Focused` state.

The code sample below shows how to change the background color of a button on focus.

```xml
<Style TargetType="Button">
    <Setter Property="VisualStateManager.VisualStateGroups">
        <VisualStateGroupList>
            <VisualStateGroup x:Name="CommonStates">
                <VisualState x:Name="Normal">
                    <VisualState.Setters>
                        <Setter Property="BackgroundColor" Value="DefaultColor" />
                    </VisualState.Setters>
                </VisualState>
                <VisualState x:Name="Focused">
                    <VisualState.Setters>
                        <Setter Property="BackgroundColor" Value="FocusedColor" />
                    </VisualState.Setters>
                </VisualState>
                <VisualState x:Name="Disabled">
                    <VisualState.Setters>
                        <Setter Property="BackgroundColor" Value="DisabledColor" />
                    </VisualState.Setters>
                </VisualState>
            </VisualStateGroup>
        </VisualStateGroupList>
    </Setter>
</Style>
```
