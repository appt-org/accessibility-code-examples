# Text truncation

Text should never get truncated in your app, even when users have enlarged their font size. Instead, apps should adapt the interface to the available space.

## WCAG

Relates to 1.4.4

## Android

On Android, you can avoid text truncation by removing all instances of [`android:maxLines`](https://developer.android.com/reference/android/widget/TextView#attr_android:maxLines) from your app. You should also avoid using fixed values for any heights or widths and instead use [`wrap_content`](https://developer.android.com/reference/android/view/ViewGroup.LayoutParams#WRAP_CONTENT) where possible.

```xml
<TextView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="Avoid text truncation" 
    android:maxLines="REMOVE" />
```

## iOS

On iOS, you can avoid text truncation by removing all instances of [`maxNumberOfLines`](https://developer.apple.com/documentation/uikit/nstextcontainer/1444531-maximumnumberoflines) from your app. You should also avoid using fixed values for any heights or widths and instead use [`constraints`](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AutolayoutPG/WorkingwithConstraintsinInterfaceBuidler.html) and [`self-sizing`](https://developer.apple.com/documentation/uikit/uifont/creating_self-sizing_table_view_cells).

```swift
let label = UILabel()
label.text = "Avoid text truncation"
label.maxNumberOfLines = REMOVE
```

## Flutter

In Flutter, you can avoid text truncation by removing all instances of [`maxLines`](https://api.flutter.dev/flutter/widgets/Text/maxLines.html) from your app. You should also set [`overflow`](https://api.flutter.dev/flutter/widgets/Text/overflow.html) to [`TextOverflow.visible`](https://api.flutter.dev/flutter/painting/TextOverflow.html#visible)  where needed. Lastly, avoid using fixed values for any heights or widths.

```dart
Text(
    'Avoid text truncation',
    maxLines: REMOVE,
    overflow: TextOverflow.visible
)
```

## React Native

In React Native, you can avoid text truncation by removing all instances of [`numberOfLines`](https://reactnative.dev/docs/text#numberoflines) from you rapp.

```jsx
<Text numberOfLines="{REMOVE}">
    Avoid text truncation
</Text>
```

## Xamarin

When using Xamarin.Forms, you can avoid text truncation by removing all instances of [`MaxLines`](https://learn.microsoft.com/en-us/dotnet/api/xamarin.forms.label.maxlines?view=xamarin-forms) from your app.

```xml
<Label
    Text="Avoid text truncation"
    MaxLines="REMOVE" />
```
