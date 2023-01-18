# Accessibility state

An accessibility state helps users of assistive technologies to understand the state of elements on the screen. The state `selected` for example, indicates that an element has been selected. The screen reader announces the state of elements as it reads the screen. It is important to assign correct states of elements to avoid misunderstanding.

## WCAG

Relates to 4.1.2

## Android

On Android, you can use the [`setAccessibilityDelegate`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityDelegate(android.view.View,androidx.core.view.AccessibilityDelegateCompat)) method of [`ViewCompat`](https://developer.android.com/reference/androidx/core/view/ViewCompat) to get a reference to [`AccessibilityNodeInfoCompat`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat). This object contains many useful accessibility related methods.

You can set an accessibility state by using the [`setStateDescription`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setStateDescription(java.lang.CharSequence)) method. A convenience method is available in `ViewCompat`, which is also named  [`setStateDescription`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setStateDescription(android.view.View,java.lang.CharSequence)).

You can also use the [`setChecked`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setChecked(boolean)) method to indicate a checked state and the [`setSelected`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setSelected(boolean)) method to indicate a selected state.

```kotlin
ViewCompat.setStateDescription(view, "Expanded")

ViewCompat.setAccessibilityDelegate(
    view,
    object : AccessibilityDelegateCompat() {
        override fun onInitializeAccessibilityNodeInfo(
            host: View,
            info: AccessibilityNodeInfoCompat
        ) {
            super.onInitializeAccessibilityNodeInfo(host, info)

            // Custom state
            info.stateDescription = "Expanded"

            // Checked
            info.isChecked = true

            // Selected
            info.isSelected = true
        }
    }
)
```

## iOS

On iOS, the [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits) attribute can be used to indicate the accessibility state. The traits  [`selected`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620197-selected) and [`notEnabled`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620208-notenabled) can be used to indicate the current state.

Other values are listed in the  [`UIAccessibilityTraits`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits) structure.

```swift
element.accessibilityTraits = .selected
element.accessibilityTraits = .notEnabled
```

## Flutter

With Flutter, you can use [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) to indicate the accessibility state. The [`Semantics constructor`](https://api.flutter.dev/flutter/widgets/Semantics/Semantics.html) contains all available options, such as `checked`, `enabled`, `hidden`, `selected` and `toggled`, among others.

```dart
Semantics(
  checked: true,
  enabled: true,
  hidden: true,
  selected: true,
  toggled: true,
  child: Widget(...)
);
```

## React Native

In React Native you can use the [`accessibilityState`](https://reactnative.dev/docs/accessibility#accessibilitystate) prop to set the accessibility state of an element. Available roles include `disabled`, `selected`, `checked`, `busy` and `expanded`, among others.

```jsx
<Pressable 
  accessibilityState="disabled|selected|checked|busy|expanded" />
```

## Xamarin

Xamarin Forms does not have built-in support to indicate the accessibility state. By using [`Effects`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/effects/introduction) it is possible to implement platform specific behaviour.

```xml
Not available, contribute!
```
