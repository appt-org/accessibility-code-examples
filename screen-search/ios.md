# Search functionality - iOS

On iOS, you could use a [`UISearchBar`](https://developer.apple.com/documentation/uikit/uisearchbar) to search for screens.

```swift
extension SearchController: UISearchBarDelegate {
    func searchBar(searchBar: UISearchBar, textDidChange searchText: String) {
        // Search
    }
}
```
