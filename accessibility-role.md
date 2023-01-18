# Accessibility role

An accessibility role helps users of assistive technologies to understand the purpose of elements on the screen. The role `button` for example, indicates that an action will be performed on activation. The screen reader announces the role of elements as it reads the screen. It is important to assign correct roles to elements to avoid misunderstanding.

## WCAG

Relates to 1.3.1, 4.1.2

## Android

On Android, you can use the [`setAccessibilityDelegate`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityDelegate(android.view.View,androidx.core.view.AccessibilityDelegateCompat)) method of [`ViewCompat`](https://developer.android.com/reference/androidx/core/view/ViewCompat) to get a reference to [`AccessibilityNodeInfoCompat`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat). This object contains many useful accessibility related methods.

You can set a role using the [`setRoleDescription`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setRoleDescription(java.lang.CharSequence)) method. However, we recommend using the [`setClassName`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setClassName(java.lang.CharSequence)) method over `setRoleDescription` to support multilingual roles. For example, set `Button::class.java.name` if an element behaves like a button. The role will be set to `Button` in English, and to its respective translation in other languages.

You can indicate a heading by using the [`setHeading`](https://developer.android.com/reference/androidx/core/view/accessibility/AccessibilityNodeInfoCompat#setHeading(boolean)) method. `ViewCompat` also contains a convenience method: [`setAccessibilityHeading`](https://developer.android.com/reference/androidx/core/view/ViewCompat#setAccessibilityHeading(android.view.View,%20boolean)).

```kotlin
ViewCompat.setAccessibilityDelegate(
    element,
    object : AccessibilityDelegateCompat() {
        override fun onInitializeAccessibilityNodeInfo(
            host: View,
            info: AccessibilityNodeInfoCompat
        ) {
            super.onInitializeAccessibilityNodeInfo(host, info)

            // Custom
            info.roleDescription = "Custom role"

            // Button
            info.className = Button::class.java.name

            // Heading
            info.isHeading = true

            // Image
            info.className = ImageView::class.java.name
        }
    }
)

// Convenience method
ViewCompat.setAccessibilityHeading(view, true)
```

## iOS

On iOS, the [`accessibilityTraits`](https://developer.apple.com/documentation/objectivec/nsobject/1615202-accessibilitytraits) attribute is used to indicate an accessibility role. The [`UIAccessibilityTraits`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits) structure contains all options, such as [`header`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620170-header), [`button`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620194-button), [`link`](https://developer.apple.com/documentation/uikit/uiaccessibility/uiaccessibilitytraits/1620178-link) and [`image`](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/1620174-image), among others.

```swift
element.accessibilityTraits = .button
element.accessibilityTraits = .header
element.accessibilityTraits = .link
element.accessibilityTraits = .image
```

## Flutter

For some widgets in Flutter, the role is assignd automatically. This happens, for example, with Flutter's buttons and text fields. If this is not the case, you can use [`Semantics`](https://api.flutter.dev/flutter/widgets/Semantics-class.html) to indicate a role. The [`Semantics constructor`](https://api.flutter.dev/flutter/widgets/Semantics/Semantics.html) contains all available options, such as `button`, `header`, `link` and `image`, among others.

```dart
Semantics(
  button: true,
  header: true,
  link: true,
  image: true,
  child: Widget(...)
);
```

## React Native

In React Native you can use the [`accessibilityRole`](https://reactnative.dev/docs/accessibility#accessibilityrole) prop to set the accessibility role of an element. Available roles include `button`, `header`, `link` and `image`, among others.

```jsx
<Pressable 
  accessibilityRole="button|header|link|image" />
```

## Xamarin

Xamarin Forms does not have built-in support for setting an accessibility role.

By using [`Effects`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/app-fundamentals/effects/introduction) it is possible to implement platform specific behaviour.

The [`SemanticEffect`](https://github.com/xamarin/XamarinCommunityToolkit/blob/main/src/CommunityToolkit/Xamarin.CommunityToolkit/Effects/Semantic/SemanticEffect.shared.cs) file inside the [`Xamarin.CommunityToolkit`](https://github.com/xamarin/XamarinCommunityToolkit) defines various methods to set accessibility roles.

```xml
<controls:CustomFontLabel
    xct:SemanticEffect.HeadingLevel="1"
    xct:SemanticEffect.Description="Button" />
```
