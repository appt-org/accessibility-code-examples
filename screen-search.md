# Search functionality

Users might have difficulty finding a specific screen. For example, inside a banking app, there might be a setting for enabling contactless payments. Users likely need to navigate through multiple screens to reach before reaching this setting. It helps to offer search functionality to jump directly to this screen.

## WCAG

Relates to 2.4.5

## Android

On Android, you could use a [`SearchView`](https://developer.android.com/reference/androidx/appcompat/widget/SearchView) to search for screens.

```kotlin
searchView.setOnQueryTextListener(
    object : SearchView.OnQueryTextListener {
        override fun onQueryTextSubmit(query: String?): Boolean {
            // Search
            return false
        }
    }
)
```

## iOS

On iOS, you could use a [`UISearchBar`](https://developer.apple.com/documentation/uikit/uisearchbar) to search for screens.

```swift
extension SearchController: UISearchBarDelegate {
    func searchBar(searchBar: UISearchBar, textDidChange searchText: String) {
        // Search
    }
}
```

## Flutter

In Flutter, you could use a [`TextField`](https://api.flutter.dev/flutter/material/TextField-class.html) to search for screens.

```dart
TextField(
  onChanged: (text) {
    // Search
  },
),
```

## React Native

In React Native, you could use a [`SearchBar`](https://reactnativeelements.com/docs/components/searchbar) to search for screens.

```jsx
<SearchBar
    onChangeText={search}
/>
```

## Xamarin

In Xamarin, you could use a [`SearchBar`](https://learn.microsoft.com/en-us/xamarin/xamarin-forms/user-interface/searchbar) to search for screens.

```xml
<SearchBar TextChanged="SearchFunction" />
```
