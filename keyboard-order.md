# Keyboard order

By adjusting the keyboard order, you can provide a great experience for users that control their device using a hardware keyboard.

## WCAG

Relates to 2.1.1, 2.4.3

## Android

On Android, you can use several `focus` properties to modify the keyboard focus order.

- [`android:nextFocusForward`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusForward): set the next element to move focus to.
- [`android:nextFocusUp`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusUp): specify which element should receive focus when navigating up
- [`android:nextFocusDown`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusDown): specify which element should receive focus when navigating down
- [`android:nextFocusLeft`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusLeft): specify which element should receive focus when navigating to the left
- [`android:nextFocusRight`](https://developer.android.com/reference/android/view/View#attr_android:nextFocusRight): specify which element should receive focus when navigating to the right

```xml
<View
    android:id="@+id/notFocusable"
    android:focusable="false"/>

<EditText
    android:id="@+id/field1"
    android:focusable="true"
    android:nextFocusForward="@+id/field2"
    android:nextFocusDown="@+id/field3"
    android:nextFocusRight="@+id/field2"/>

<EditText
    android:id="@+id/field2"
    android:focusable="true"
    android:nextFocusForward="@+id/field3"
    android:nextFocusDown="@+id/field4"/>

<EditText
    android:id="@+id/field3"
    android:focusable="true"
    android:nextFocusForward="@+id/field4"/>

<EditText
    android:id="@+id/field4"
    android:focusable="true"/>
```

## iOS

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

## Flutter

In Flutter, you can use [`FocusTraversalGroup`](https://api.flutter.dev/flutter/widgets/FocusTraversalGroup-class.html)  to group widgets together. All subwidgets must be fully traversed before the keyboard focus is moved to the next widget. When grouping widgets into related groups is not enough, a [`FocusTraversalPolicy`](https://api.flutter.dev/flutter/widgets/FocusTraversalPolicy-class.html) can be set to determine the ordering within the group.

The default [`ReadingOrderTraversalPolicy`](https://api.flutter.dev/flutter/widgets/ReadingOrderTraversalPolicy-class.html) is usually sufficient, but in cases where more control over ordering is needed, an [`OrderedTraversalPolicy`](https://api.flutter.dev/flutter/widgets/OrderedTraversalPolicy-class.html) can be used. The `order` argument of the [`FocusTraversalOrder`](https://api.flutter.dev/flutter/widgets/FocusTraversalOrder-class.html) widget wrapped around the focusable components determines the order. The order can be any subclass of [`FocusOrder`](https://api.flutter.dev/flutter/widgets/FocusOrder-class.html), but [`NumericFocusOrder`](https://api.flutter.dev/flutter/widgets/NumericFocusOrder-class.html) and [`LexicalFocusOrder`](https://api.flutter.dev/flutter/widgets/LexicalFocusOrder-class.html) are provided.

Read more about [Flutter's keyboard focus system](https://docs.flutter.dev/development/ui/advanced/focus).

The example below shows how to use the `FocusTraversalOrder` widget to traverse a row of buttons in the order TWO, ONE, THREE using `NumericFocusOrder`.

```dart
Row(
    children: <Widget>[
        FocusTraversalOrder(
            order: NumericFocusOrder(2.0),
            child: TextButton(
                child: const Text('ONE'),
            ),
        ),
        const Spacer(),
        FocusTraversalOrder(
            order: NumericFocusOrder(1.0),
            child: TextButton(
                child: const Text('TWO'),
            ),
        ),
        const Spacer(),
        FocusTraversalOrder(
            order: NumericFocusOrder(3.0),
            child: TextButton(
                child: const Text('THREE'),
            ),
        ),
    ],
);
```

## React Native

React Native has implemented all Android keyboard focus properties.

- [`nextFocusForward`](https://reactnative.dev/docs/view#nextfocusforward-android): specify the next element to move focus to
- [`nextFocusUp`](https://reactnative.dev/docs/view#nextfocusup-android): specify which element should receive focus when navigating up
- [`nextFocusDown`](https://reactnative.dev/docs/view#nextfocusdown-android): specify which element should receive focus when navigating down
- [`nextFocusLeft`](https://reactnative.dev/docs/view#nextfocusleft-android): specify which element should receive focus when navigating left
- [`nextFocusRight`](https://reactnative.dev/docs/view#nextfocusright-android): specify which element should receive focus when navigating right

It seems that none of the iOS keyboard focus properties have been implemented by React Native.

```jsx
Not available, contribute!
```

## Xamarin

Xamarin Forms supports changing the keyboard order through the [`TabIndex`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.visualelement.tabindex?view=xamarin-forms) property. The default value is 0. The lower the value, the higher the priority.

The [`IsTabStop`](https://docs.microsoft.com/en-us/dotnet/api/xamarin.forms.visualelement.istabstop?view=xamarin-forms) property can be used to exclude elements from tabbed navigation.

Read more about [Keyboard Accessibility in Xamarin.Forms](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/keyboard).

The code example below shows how exclude the label from receiving keyboard focus, and how to reach the save button before reaching the cancel button.

```xml
<Label Text="Appt" IsTabStop="True" />
<Button x:Name="cancelButton" TabIndex="20" />
<Button x:Name="saveButton" TabIndex="10"/>
```
