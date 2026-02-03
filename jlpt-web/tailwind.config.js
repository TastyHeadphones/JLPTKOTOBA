/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            fontFamily: {
                'sans': ['-apple-system', 'BlinkMacSystemFont', '"Segoe UI"', 'Roboto', 'Helvetica', 'Arial', 'sans-serif'],
                'jp': ['"Hiragino Kaku Gothic ProN"', '"Hiragino Sans"', 'Meiryo', 'sans-serif'],
            },
            colors: {
                'apple-blue': '#007AFF',
                'apple-gray': '#F5F5F7',
                'apple-dark': '#1D1D1F',
                'card-bg': '#FFFFFF',
            },
            boxShadow: {
                'apple': '0 4px 12px rgba(0, 0, 0, 0.08)',
                'apple-hover': '0 8px 24px rgba(0, 0, 0, 0.12)',
            }
        }
    },
    plugins: [],
}
