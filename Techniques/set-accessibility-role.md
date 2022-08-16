# Set accessibility role

An accessibility label helps users of assistive technologies with understanding the purpose of elements on the screen. The role `button` for example, indicates that an action will be performed on activation. The screen reader announces the role of elements as it reads the screen. It is important to assign correct roles to elements to avoid misunderstanding.

## Android

On Android, you can set a custom role via the [`setRoleDescription`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setRoleDescription(java.lang.CharSequence)) method of [`AccessibilityNodeInfoCompat`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat). It is usually better to use the [`setClassName`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setClassName(java.lang.CharSequence)) method to inherit the role of an existing element. For example, set `Button::class.java.name` if an element behaves like a button.

```kotlin
ViewCompat.setAccessibilityDelegate(
    element,
    object : AccessibilityDelegateCompat() {
        override fun onInitializeAccessibilityNodeInfo(
            host: View,
            info: AccessibilityNodeInfoCompat
        ) {
            super.onInitializeAccessibilityNodeInfo(host, info)
            info.roleDescription = "Custom"
            info.className = Button::class.java.name
        }
    }
)
```

## iOS

On iOS, the [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits) attribute is used to set a role. For example, you can set the role [`button`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620194-button) or [`link`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620178-link). You can view all possible values at [`UIAccessibilityTraits`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits).

```swift
element.accessibilityTraits = .button
element.accessibilityTraits = .link
```

## Flutter

For some widgets in Flutter, the role is assignd automatically. This happens, for example, with Flutter's buttons and text fields. If this is not the case, you can use [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) to indicate a role. The [`Semantics constructor`](https://api.flutter.dev/flutter/widgets/Semantics/Semantics.html) contains all available options, such as `button`, `header`, `image`, and `link` among others.

```dart
Semantics(
  image: true,
  button: true,
  link: true,
  child: Widget(...)
);
```

## React Native

In React Native you can add an [`accessibilityRole`](https://reactnative.dev/docs/accessibility#accessibilityrole) to add a role to an element. Available roles include `button`, `header`, `image`, and `link` among others.

```jsx
<Pressable 
  accessibilityRole="button" />
```

## Xamarin

Xamarin Forms does not have built-in support for setting an accessibility role. By using [`Effects`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/effects/introduction) it is possible to implement platform specific behaviour. The [`A11YEffect`](https://github.com/appt-org/accessibility-code-examples/blob/main/Xamarin/en/A11yEffect.md), [`A11YEffect for Android`](https://github.com/appt-org/accessibility-code-examples/blob/main/Xamarin/en/A11yEffect_Android.md) and [`A11YEffect for iOS`](https://github.com/appt-org/accessibility-code-examples/blob/main/Xamarin/en/A11yEffect_iOS.md) files show how to implement an `effect` for accessibility role.

```xml
<controls:CustomFontLabel
    effects:A11YEffect.ControlType="{OnPlatform iOS=Button, Android=None}" />
```
