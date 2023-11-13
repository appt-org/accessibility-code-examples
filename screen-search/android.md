# Search functionality - Android

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
