# Dark mode - React Native

With React Native, you can detect dark mode by checking if the [`Appearance.getColorScheme()`](https://reactnative.dev/docs/appearance#getcolorscheme) method returns `dark`.

When defining a [`ThemeProvider`](https://reactnativeelements.com/docs/customization/themprovider) you can return a different theme when dark mode is active.

```jsx
import { useColorScheme } from 'react-native';
import { ThemeProvider } from 'styled-components';

const darkTheme = {
    primary: "#f967e9",
};
    
const lighTheme = {
    primary: "#cc00b9"
};

const App: React.FC = () => {
    const scheme = useColorScheme();
    return (
    <ThemeProvider theme={scheme === 'dark' ? darkTheme : lightTheme}>
        {props.children}
    </ThemeProvider>
    );
}

export default App;
```
