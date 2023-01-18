# Reflow

Content on the screen should reflow based on the users' preferences.  In landscape mode, the vertical space is much smaller compared to portrait mode. And when users have enlarged their font size, text should not get truncated. Instead, apps should adapt the interface to the available space.

## WCAG

Relates to 1.4.10

## Android

On Android, all elements should be placed in a scrollable layout, such as a [`ScrollView`](https://developer.android.com/reference/android/widget/ScrollView) or [`RecyclerView`](https://developer.android.com/jetpack/androidx/releases/recyclerview). Never use fixed values for any heights or widths.

```xml
<ScrollView
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Content should scroll!" />
</ScrollView>
```

## iOS

On iOS, all elements should be placed in a scrollable layout, such as [`UIScrollView`](https://developer.apple.com/documentation/uikit/uiscrollview), [`UITableView`](https://developer.apple.com/documentation/uikit/views_and_controls/table_views) or [`UICollectionView`](https://developer.apple.com/documentation/uikit/views_and_controls/collection_views). Never use fixed values for any heights or widths.

```swift
let label = UILabel()
label.text = "Content should scroll!"

let view = UIView()
view.addSubview(label)

let scrollView = UIScrollView()
scrollView.addSubview(view)
```

## Flutter

In Flutter, all elements should be placed in a scalable widget, such as [`SingleChildScrollView`](https://api.flutter.dev/flutter/widgets/SingleChildScrollView-class.html) or [`ListView`](https://api.flutter.dev/flutter/widgets/ListView-class.html). These widgets ensures that underlying widgets will become scrollable, in case they do not fit on the screen.

```dart
SingleChildScrollView(
  child: Text(
    'Content should scroll!',
    softWrap: true,
    overflow: TextOverflow.visible,
  ),
)
```

## React Native

In React Native, your elements should be placed inside a scrollable layout, such as [`ScrollView`](https://reactnative.dev/docs/scrollview). If the elements don't fit, the view becomes scrollable over the vertical axis so the user can still reach them. Ideally scrolling is only necessary in one direction.

```jsx
<ScrollView>
    <Text>
        Content should scroll!
    </Text>
</ScrollView>
```

## Xamarin

When using Xamarin.Forms, your elements should be placed inside a scrollable layout, such as:

- [`ScrollView`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/layouts/scrollview): for static content
- [`CollectionView`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/collectionview/): for multi dimensional content
- [`ListView`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/listview/): for one dimensional content
- [`WebView`](https://docs.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/webview): for web content

```xml
<ScrollView>
    <Label Text="Content should scroll!" />
</ScrollView>
```
