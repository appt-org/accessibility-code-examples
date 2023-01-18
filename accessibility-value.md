# Accessibility value

An accessibility value helps users of assistive technologies to understand the state of elements on the screen. A slider should indicate the currently selected value, and ideally also it's minimum and maximum value. The screen reader announces the value of elements as it reads the screen. It is important to assign correct values to elements to avoid misunderstanding.

## WCAG

Relates to 4.1.2

## Android

Android has limited support to provide a dedicated accessibility value for assistive technologies. The [`AccessibilityNodeInfoCompat`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat) object contains a couple of methods, such as the [`setChecked`](https://developer.android.com/reference/kotlin/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setchecked) method.

Unfortunately the desired value is often not available. If your desired value is not included, you can append it to the [`contentDescription`](https://developer.android.com/reference/android/view/View.html#attr_android:contentDescription) attribute.

```kotlin
ViewCompat.setAccessibilityDelegate(
    element,
    object : AccessibilityDelegateCompat() {
        override fun onInitializeAccessibilityNodeInfo(
            host: View,
            info: AccessibilityNodeInfoCompat
        ) {
            super.onInitializeAccessibilityNodeInfo(host, info)
            info.isChecked = true
        }
    }
)

element.contentDescription = "Name (Value)"
```

## iOS

On iOS, you can set an accessibility value with the [`accessibilityValue`](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/1619583-accessibilityvalue) or [`accessibilityAttributedValue`](https://developer.apple.com/documentation/objectivec/nsobject/2866105-accessibilityattributedvalue/) property.

When using the semantically correct element, you usually do not need to modify the `accessibilityValue`. For example, a [`UISwitch`](https://developer.apple.com/documentation/uikit/uiswitch) sets the `accessibilityValue` to `selected` or `not selected` and a [`UISlider`](https://developer.apple.com/documentation/uikit/uislider) sets the `accessibilityValue` to the current value. If the default value is incorrect or unclear, you can override the value manually.

```swift
element.accessibilityValue = "Custom"
```

## Flutter

With Flutter, you can set an accessibility value by using the `value` or `attributedValue` property of [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics/Semantics.html).

When using the semantically correct element, you usually do not need to modify the accessibility value. For example, [`Slider`](https://api.flutter.dev/flutter/material/Slider-class.html), [`Switch`](https://api.flutter.dev/flutter/material/Switch-class.html) and [`CheckBox`](https://api.flutter.dev/flutter/material/Checkbox-class.html), and others automatically assign accessibiluty values.

It is also possible to set an `increasedValue` and `decreasedValue` or `attributedDecreasedValue` and `attributedIncreasedValue` to indicate what the value will become when the user decreases or increases the value.

Some widgets include additional methods, such as [`semanticFormatterCallback`](https://api.flutter.dev/flutter/material/Slider/semanticFormatterCallback.html).

```dart
Semantics(
  value: 'Custom',
  increasedValue: 'Custom + 1',
  decreasedValue: 'Custom - 1',
  child: Widget(),
);      
```

## React Native

In React Native you can use the [`accessibilityValue`](https://reactnative.dev/docs/accessibility#accessibilityvalue) and [`accessibilityState`](https://reactnative.dev/docs/accessibility#accessibilitystate) props to set an accessibility value. The `accessibilityValue` indicates the current value of a component. You can indicate a range, using `min`, `max`, and `no`, or text using `text`. The `accessibilityState` indicates the current state of a component, for example `disabled` or `checked`.

```jsx
<View
  accessibilityValue={{min: 0, max: 100, now: 50}}
  accessibilityState="busy" />

<View 
  accessibilityValue={{text: "Custom"}}
  accessibilityState="disabled" />
```

## Xamarin

Xamarin Forms elements such as [`Button`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/button) and [`Entry`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/text/entry) automatically include an accessibility value. When you make custom elements you have to set these properties yourself.

However, there is no dedicated property to set an accessibility value. You can embed the value inside the label by using [`MultiBinding`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/data-binding/multibinding) inside the [`AutomationProperties.Name`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/accessibility/automation-properties#automationpropertiesname) property.

```xml
<Label
    <AutomationProperties.Name>
        <MultiBinding StringFormat="{}{0}, {1}">
            <Binding Source="The value is: " />
            <Binding Source="{BindingValue}" />
        </MultiBinding>
    </AutomationProperties.Name>
</Label>
```
