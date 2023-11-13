# Reflow - Xamarin

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
